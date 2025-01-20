---
created: 2025-01-10T10:57:15
source: "https://www.ffutop.com/posts/2021-03-15-datetime-vs-calendar/"
type: "archive-web"
modified: 2025-01-15T11:38:19
---

一个特殊的日期 (`1988-04-10`, 字段类型 `date`)，从数据库尝试读取却始终抛出异常 `HOUR_OF_DAY: 0->1` 。最初百思不得其解，其后发现这个日期恰好是夏令时的起始日，而后又纠结于 1988 年夏令时“从 04 月 10 日早晨 2 时起，将时针往前拨一小时，即二时变三时”。

## 重现

```java
import java.sql.Timestamp;
import java.util.*;

/**
 * HINT: 适用于 java -version < 8u201 or 7u211 
 * @author fangfeng
 * @date 2021-03-15
 */
public class Main {

    public static void main(String[] args) {
        Calendar cal = Calendar.getInstance(TimeZone.getTimeZone("Asia/Shanghai"), Locale.US);
        cal.setLenient(false);
        cal.set(1988, Calendar.APRIL, 10, 0, 0, 0);
        Timestamp ts = new Timestamp(cal.getTimeInMillis());
        System.out.println(ts);
    }
}

/**
 * HINT: 适用于 java -version >= 8u201 or 7u211 
 * @author fangfeng
 * @date 2021-03-15
 */
public class Main {

    public static void main(String[] args) {
        Calendar cal = Calendar.getInstance(TimeZone.getTimeZone("Asia/Shanghai"), Locale.US);
        cal.setLenient(false);
        cal.set(1988, Calendar.APRIL, 17, 2, 0, 0);
        Timestamp ts = new Timestamp(cal.getTimeInMillis());
        System.out.println(ts);
    }
}
```

```shell
[ffutop@ffutop /]$ java -cp . Main
Exception in thread "main" java.lang.IllegalArgumentException: HOUR_OF_DAY: 0 -> 1
	at java.util.GregorianCalendar.computeTime(GregorianCalendar.java:2829)
	at java.util.Calendar.updateTime(Calendar.java:3393)
	at java.util.Calendar.getTimeInMillis(Calendar.java:1782)
	at Main.main(Main.java:15)

[ffutop@ffutop /]$ java -version
java version "1.8.0_161"
Java(TM) SE Runtime Environment (build 1.8.0_161-b12)
Java HotSpot(TM) 64-Bit Server VM (build 25.161-b12, mixed mode)
```

## 原因分析

`Calendar` 基于配置的时区 (`cal.getTimeZone()`) 对日历时间加以描述。通过一系列 `set(...)` 完成描述之后，利用 `Calendar.getTimeInMillis()` 方法获取所描述时间的时间戳（时间戳是相对于格林威治时间 1970 年 1 月 1 日 0 时 0 分 0 秒相差的毫秒数）。

其中 `getTimeInMillis()` 触发了 `computeTime()` ，分五个步骤（其中第 1、5 步只有配置了 calendar.setLenient(false) 才会执行）

```java
protected void computeTime() {
    // 1. 快照配置的各项日历字段
    if (!isLenient()) {
        if (originalFields == null) {
            originalFields = new int[FIELD_COUNT];
        }
        for (int field = 0; field < FIELD_COUNT; field++) {
            int value = internalGet(field);
            originalFields[field] = value;
        }
    }

    // 2. 计算基于当前时区1970年1月1日0时0分0秒的毫秒数
    // millis represents local wall-clock time in milliseconds.
    long millis = (fixedDate - EPOCH_OFFSET) * ONE_DAY + timeOfDay;

    // 3. 将毫秒数基于 Calendar 配置的时区和夏令时，调整成基于 GMT 1970-01-01 00:00:00 的时间戳
    zoneOffsets[0] = internalGet(ZONE_OFFSET);
    zoneOffsets[1] = internalGet(DST_OFFSET);
    // Adjust the time zone offset values to get the UTC time.
    millis -= zoneOffsets[0] + zoneOffsets[1];
    time = millis;

    // 4. 逆向将时间戳转换成当前时区及夏令时下的日期描述
    int mask = computeFields(fieldMask | getSetStateFields(), tzMask);

    // 5. 确认每个用户主动配置的日历描述字段是否与计算的不同
    if (!isLenient()) {
        for (int field = 0; field < FIELD_COUNT; field++) {
            if (!isExternallySet(field)) {
                continue;
            }
            if (originalFields[field] != internalGet(field)) {
                String s = originalFields[field] + " -> " + internalGet(field);
                // Restore the original field values
                System.arraycopy(originalFields, 0, fields, 0, fields.length);
                throw new IllegalArgumentException(getFieldName(field) + ": " + s);
            }
        }
    }
    setFieldsNormalized(mask);
}
```

遇到的错误，恰恰是发生在第 5 步，夏令时导致日历跳过了对中国标准时间 1988 年 4 月 10 日 0 时 0 分 0 秒的描述，自 1988 年 4 月 9 日 23 时 59 分 59 秒后的下一秒被直接描述成了 1988 年 4 月 10 日 1 时 0 分 0 秒。因此，在时区被配置为 `Asia/Shanghai` 时，由于是夏令时的起始时间，日历描述的时间 (0 时) 不存在，在 Calendar 的处理过程中，被标准化成了 1 时。严格模式下的 Calendar 认为这是非法描述，抛出了异常。

## 解决方案

1. 将时区配置调整成 $GMT+8$，中国标准时间在特定的几年有夏令时的问题，但东八区没有，就不会触发这个问题。
2. 在复现问题时也发现，高版本 JDK 对夏令时的起始时间描述不同。针对这个现象，可以升级 JDK ，数据库的 `date` 读取到应用中会被填充上时间 0 时 0 分 0 秒，而新版本的夏令时切换时间是 2 时，自动规避了这个问题。

夏令时的起止，是政令对日历描述的人为干预。每年均可能发生变化，JDK 如何感知这个规律并在系统上加以体现呢？无它，穷举所有变化，并配置在 JDK 中。详见：[Timezone Data Versions in the JRE Software](https://www.oracle.com/java/technologies/tzdata-versions.html)

不同版本下 Asia/Shanghai 时区夏令时起始时间的不同，正是源于这种穷举配置，早期维护者认为中国标准时间的夏令时切换发生在 0 时，而后来又经证明发生在 2 时，新版本 JDK 及时修正了这个问题罢了。

![JRE Timezone Data Change Log](https://img.ffutop.com/76CA5CD1-41A7-469E-AAB0-BC1D69668C55.png)
