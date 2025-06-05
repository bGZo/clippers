---
created: 2024-01-06T12:00:00
source: https://blog.azurezeng.com/installation-guide-for-archlinux-kde/
type: archive-web
modified: 2025-01-15T11:38:16
---

## Arch Linux+KDE 安装流程和踩坑记录 – Azure Zeng Blog

  由于对 Ubuntu 的 Snap Store 存在不满，并且自己也想整一个个性化，最新内核，并且能做到所有安装的功能都用在刀刃上的 Linux，于是这段时间对 Arch Linux 进行了一些研究。当然，学到了很多。

  由于目前我的笔记本不适合安装 Linux 系统，故这次所有的操作都在虚拟机下完成。

  这篇文章也算是根据自己的踩坑记录进行编写。

  这里建议 UEFI+GPT，因为这是目前现代硬件更加推荐的配置。

  在管理硬盘启动项这方面，Legacy BIOS+MBR 的启动项管理方式个人觉得非常抽象，但是 UEFI+GPT 管理启动项理解起来会相对简单。

==MBR 分区表限制 4 个主分区 (但是扩展分区中可以有无数分区)，GPT 则限制 128 个分区 (无主分区和扩展分区的区别)。针对大容量硬盘的支持，则 GPT 更胜一筹。==

另外，现在出厂预装 Windows 的笔记本，均会使用 UEFI+GPT，此时双系统方案也就建议使用 UEFI+GPT 了。

  总结：如果是现代硬件和虚拟机程序，如果支持 UEFI+GPT 则无脑用 UEFI+GPT。本文也只讨论 UEFI+GPT 这种情况。

  访问这里，即可获取本月的 Arch Linux 启动盘 ISO 文件：[https://archlinux.org/download/](https://archlinux.org/download/)。

==该 ISO 文件每月第一天会更新一次。为了保证启动盘启动的 Arch Linux 不会出一些奇怪的问题 (比如 keyring 问题)，在安装好 Arch Linux 系统之后也是建议定期更新启动盘 ISO 文件。==

同时，对于一些疑难杂症，[ArchWiki](https://wiki.archlinux.org/) 也是一个好东西。当然，ArchWiki 中也有 [完善的安装指引文章](https://wiki.archlinux.org/title/Installation_guide)，对于 Arch Linux 新手，如果能看懂则会有很大帮助。

  对于虚拟机，将 ISO 载入到虚拟机即可。

  对于实体机，则需要将其写入到 U 盘中。你也可以使用 Ventoy，这样处理和更新 Arch Linux ISO 会更加方便。

  关于 Windows 11 的安全启动 (Secure Boot) 问题

  进入 GRUB 界面时，默认选择第一项。

  ![](https://i.imgtg.com/2023/01/04/GhthF.png)

  当你进入这个界面时，就代表 Arch Linux ISO 已经启动完成，可以开始操作了。

  ![](https://z1.ax1x.com/2023/01/09/pSeMeVx.png)

  如果你的电脑或笔记本已经接入了有线网络，则可以直接开始下一步操作。

  对于 WiFi 用户，需要通过 `iwctl` 命令手动联网。

  请注意，如果使用实体机安装，尽量不要使用需要浏览器认证才能使用的网络，比如部分校园网。因为此时很难使用浏览器进行验证操作。

  如果你有两台电脑，或者虚拟机安装 Arch Linux，可以考虑通过 SSH 的方式来进行接下来的安装。

  Arch Linux ISO 启动的系统支持使用远程 SSH 进行系统配置。如果确实要这么做，请确保 Arch Linux ISO 启动的系统已经正确联网，同时 (如果你是实体机安装) 建议两台电脑位于同一网络下，且两台电脑可通过这个网络互相连接 (有些校园网共用 WiFi 可能存在设备隔离，即使两台设备在同一 WiFi 下，也无法互相连接)。

  ```zsh
  # 设置root用户的密码，不设置将无法使用SSH连接
  passwd
  # 获取当前系统的IP地址
  ip addr
  ```

  在 `ip addr` 命令的输出结果中找到当前系统的 IP 地址，然后使用另外一台电脑的 SSH 连接即可 (使用 root 账户)。

  ![](https://z1.ax1x.com/2023/01/09/pSeMYZt.png)

  这里推荐使用 `cfdisk` 进行分区操作。

  如果你有使用 btrfs 文件系统的打算，则建议同时阅读这篇文章：[Arch Linux + btrfs 配置简明指南](https://blog.azurezeng.com/archlinux-with-btrfs-simple-guide/)。

  ```zsh
  # 请将/dev/nvme0n1更换为你自己的硬盘，比如/dev/sda。
  # 由于此处我用的是VMware虚拟机模拟出了NVMe，此处填写NVMe硬盘位置。
  cfdisk /dev/nvme0n1
  ```

  如果是第一次操作硬盘，会出现这个界面。由于我们正在讨论 UEFI+GPT 方案，所以此步选择 gpt。

  Legacy BIOS+MBR 方案用户需要选择 dos 选项。

  ![](https://z1.ax1x.com/2023/01/05/pSkEqgO.png)

  此时将正式进入 `cfdisk` 的分区界面。这种可视化 UI 界面应该很好上手。

  ![](https://z1.ax1x.com/2023/01/05/pSkEjDH.png)

接下来，是一些常见的分区方案：

  对于大部分虚拟机：

  | 分区编号 | 分区大小 | 文件系统 | 挂载点 | 备注 |
  | --- | --- | --- | --- | --- |
  | 1 | 100MB | FAT32 | /efi | EFI 分区 |
  | 2 | 所有剩余空间 | ext4 | / | Linux 根目录分区 |

具有大容量硬盘（此处定义为容量 512+GB 的磁盘）时：

  | 分区编号 | 分区大小 | 文件系统 | 挂载点 | 备注 |
  | --- | --- | --- | --- | --- |
  | 1 | 100MB | FAT32 | /efi | EFI 分区，准备双系统的请注意下方的注意事项 |
  | 2 | 推荐 150+GB | ext4 | / | Linux 根目录分区，此分区大小合理分配 |
  | 3 | 所有剩余空间 | ext4 | /home | 用户目录分区 |

需要注意一点：如果你准备安装 Windows+Arch Linux 双系统，此时 Windows 已经帮你建立好 EFI 分区了，此时请勿再新建新的 EFI 分区，直接使用 Windows 的 EFI 分区即可。这种情况下请仔细操作 EFI 分区，错误的操作导致 Windows EFI 文件损坏，将导致 Windows 无法启动。

  在新建 EFI 分区时，需要选择下方的 `Type` 选项，修改分区类型为 `EFI System`。

  ![](https://z1.ax1x.com/2023/01/05/pSkZUmQ.png)

  这是个人在虚拟机中的选择的分区方案。

  ![](https://z1.ax1x.com/2023/01/05/pSkZdTs.png)

  选择下方的 Write 选项，保存分区表，即可退出 cfdisk。

  接下来，我们需要格式化并将挂载分区。

  ```zsh
  # 需要格式化的硬盘千万不要输错！下面的硬盘只是示例。
  mkfs.fat -F 32 /dev/nvme0n1p1
  mkfs.ext4 /dev/nvme0n1p2
  mkfs.ext4 /dev/nvme0n1p3
  # 接下来挂载分区，通常推荐临时将硬盘挂载到/mnt目录下。
  # 一定要按照顺序挂载，通常的挂载顺序为顶级目录，然后再挂载次级目录。
  # 比如一个合理的挂载顺序是/mnt -> /mnt/boot -> /mnt/boot/efi
  # 不按照顺序挂载的结果就是挂载顺序错误的部分目录无法访问，后续生成的fstab数据也会有问题。
  # 如果出现这种情况，一定要umount卸载挂载点，再重新进行挂载。
  mount --mkdir /dev/nvme0n1p3 /mnt
  mount --mkdir /dev/nvme0n1p2 /mnt/boot
  mount --mkdir /dev/nvme0n1p1 /mnt/efi
  ```

  更新 mirrorlist 以获取最佳下载速度。

  如果你不在中国大陆，记得修改下面命令的国家代码来获取你所在国家的 mirrorlist。

  ```zsh
  # 通过获取ArchLinux官方mirrorlist来更新镜像列表
  # 若使用本方法，记得编辑/etc/pacman.d/mirrorlist启用相应的镜像站
  curl -o /etc/pacman.d/mirrorlist https://archlinux.org/mirrorlist/?country=CN&protocol=https
  # 或者，通过reflector直接获取最新的mirrorlist
  reflector -c China -l 10 --sort rate --save /etc/pacman.d/mirrorlist
  ```

  接下来可以修改 `/etc/pacman.conf` 来优化下载速度。

  具体操作为，取消 `ParallelDownloads` 这个设置的注释。如果你想，还可以修改这个设置后面的数值 (注意必须合理)，来增加同时下载的软件包数量。

  同时你还可以取消 `Color` 选项的设置，让 pacman 启用彩色输出。

  ![](https://z1.ax1x.com/2023/01/05/pSAGddP.png)

  上述操作做完后，我们就可以正式开始安装 Arch Linux 了。

  ```zsh
  # 每次用ArchLinux ISO执行新系统安装前，建议更新当前系统的Keyring
  # 每次用ISO启动，只需要执行一次
  # 之前就出现过Keyring未更新导致OpenSSL包死活装不上的事情
  pacman -Sy archlinux-keyring
  # 通过pacstrap在/mnt目录下初始化keyring并安装软件包
  # 注意，执行这段命令的同时，会将你当前启动的ArchLinux的/etc/pacman.d/mirrorlist
  # 也复制到/mnt目录下
  pacstrap -K /mnt base [packages]
  ```

  将 `packages` 参数换成你需要的包。对于初次接触 Arch Linux 的读者，稍候会给出一些选择软件包的提示。

  如果后面发现少装了什么包，可以在后面 `arch-chroot` 后使用 `pacman`，或者使用 `pacman -r /mnt -S packages` 进行安装。

  ```zsh
  # 这段安装代码只是示例，请根据自己的实际需要修改。
  # 此处安装linux-firmware和intel-ucode，因为我们假定使用Intel CPU实体机安装。
  # 但是编写本文时的实际环境为VMware Workstation虚拟机，因此同时安装open-vm-tools。
  pacstrap -K /mnt base linux base-devel linux-firmware intel-ucode pipewire-audio pipewire-alsa pipewire-pulse pipewire-jack \
  wireplumber alsa-utils man-db man-pages texinfo networkmanager vi vim git zsh open-vm-tools bluez bluez-utils reflector
  ```

  你也可以把后面步骤的需要的软件包在这个阶段就安装上去进行，只需要把这些包加到这一步的 `packages` 参数中。

  安装系统的过程可能取决于你电脑的速度和网速。

  对于第一次接触 Arch Linux 的用户，选择需要的包可能是一件难题。这里将给出一些提示。

  对于所有的 Arch Linux 都应该安装的包：`base`(Arch Linux 核心包，**必须安装**)，`base-devel`(这个包可能会在使用 AUR 软件源的时候用上)，`sudo`(如果没安装 `base-devel` 则该包必须安装，否则配置好后无法使用 root 权限执行命令)

  选择一个 Linux 内核：正常情况下从 `linux` 和 `linux-lts` 这两个常用内核选一个。其他内核可以去 [这里](https://wiki.archlinux.org/title/Kernel) 查看。

  一些驱动相关的软件包：`linux-firmware`(实体机必须安装，否则等下进系统将会出现各种缺驱动的问题，虚拟机不用)，`alsa-utils`(推荐安装，管理声卡相关工具)

  声音相关的软件包则有两组：PipeWire (正常情况下推荐这个)，PulseAudio，二选一。使用桌面环境的用户建议安装，否则声音相关的功能可能出问题。

  PipeWire：`pipewire-audio`，`pipewire-alsa`，`pipewire-pulse`，`pipewire-jack`，`wireplumber`

  PulseAudio：`pulseaudio`，`pulseaudio-alsa`，`pulseaudio-bluetooth`(使用蓝牙则需要这个包)

  网络管理：`networkmanager`(若使用桌面环境则建议直接安装这个，服务器的 Arch Linux 可以考虑 `systemd-networkd` 和 `systemd-resolved`)

  帮助文档相关包: `man-db`，`man-pages`，`texinfo`

  常用的一些命令行软件，以及 Shell (根据自己的需要进行安装)：`vi`，`vim`，`nano`，`git`，`zsh` 等

  蓝牙支持：`bluez`，`bluez-utils`

  SSH 协议：`openssh`

  NTFS 读写支持：`ntfs-3g`

  VMware Tools (针对 VMware 虚拟机): `open-vm-tools`(安装后需要启用 `vmtoolsd`，`vmware-vmblock-fuse` 服务)

  最新 Arch Linux 镜像站地址获取实用程序：`reflector`

  微码修正文件 (根据你的 CPU 型号选择，虚拟机不需要安装)：`intel-ucode`(Intel CPU)，`amd-ucode`(AMD CPU)

  当上面的命令执行完成后，一个全新的 Arch Linux 系统便装好了 (但是还没配置，还不能直接拿来用)。接下来开始配置这个新安装的 Arch Linux。

  ```zsh
  # 首先使用genfstab命令生成fstab数据，并追加到新安装的ArchLinux的/etc/fstab文件中
  # 对于使用了Legacy BIOS+MBR方案的读者，请去除下面的-U参数
  genfstab -U /mnt >> /mnt/etc/fstab
  # 将根目录切换到/mnt以便进行后续配置
  arch-chroot /mnt
  # 此时已经切换到新安装的ArchLinux目录下
  # 修改计算机名称
  echo [你想要的计算机名称] >> /etc/hostname
  # 修改时区，请根据自己的需要修改时区
  # 修改好后可以输入date来确认时区修改
  ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
  # 生成本地化文件
  vim /etc/locale.gen
  # 取消该文件的注释en_US.UTF8 (必须)
  # 以及你想要的语言，比如zh_CN.UTF8
  # 如果稍后需要将界面调成中文，必须启用zh_CN.UTF8
  # 一定要保证会生成en_US.UTF8的翻译，否则初步配置系统期间可能出现字体显示错误问题。
  # 保存后执行下面的命令
  locale-gen
  # 启动必要的服务
  systemctl enable NetworkManager # 不启用则无法联网
  systemctl enable bluetooth # 如果你安装了蓝牙支持
  # 如果你安装了open-vm-tools，启用下面两个服务
  systemctl enable vmtoolsd
  systemctl enable vmware-vmblock-fuse
  # 新安装的ArchLinux的/etc/pacman.conf为默认设置
  # 如果需要，你可以按照之前的方法修改/etc/pacman.conf来优化pacman的下载和显示
  # 此处编辑过程略
  vim /etc/pacman.conf
  # 接下来处理以下sudo，否则之后sudo无法使用
  # 第一种方案是直接在/etc/sudoers.d下创建相关的文件，免去修改/etc/sudoers的一些麻烦之处
  echo "%wheel ALL=(ALL:ALL) ALL" > /etc/sudoers.d/wheel
  # 第二种方案，编辑/etc/sudoers，反正不是很推荐使用这个方案
  # /etc/sudoers默认为只读权限，需要用chmod修改权限后编辑
  chmod +w /etc/sudoers
  vim /etc/sudoers
  # 取消这行的注释：# %wheel ALL=(ALL:ALL) ALL
  # 然后保存，恢复/etc/sudoers的权限
  chmod -w /etc/sudoers
  ```

  接下来，需要创建一个自己的账户，安装结束之后，对于桌面平台，我们的大部分时间都会使用自己的账户登录系统，而不是 root。

  ```zsh
  # 把myuser换成你喜欢的用户名
  useradd -m -G wheel myuser
  # 修改密码，否则等下无法登录
  passwd myuser
  # 可选: 为root用户设置密码
  passwd
  ```

  如果需要，可以同时生成一个硬盘 swapfile（交换文件）。

  ```zsh
  # 可以把4G换成任意大小，比如2048M
  fallocate -l 4G /swapfile
  # 如果fallocate命令不能使用，才应该考虑使用下面的dd命令创建
  # 这条命令最后生成的文件大小为bs*count，请合理修改bs和count参数，这里是4GB
  dd if=/dev/zero of=/swapfile bs=1024M count=4
  # 修改权限并创建swap文件数据
  chmod 0600 /swapfile
  mkswap /swapfile
  # 写入到fstab中，实现开机挂载
  echo '/swapfile swap swap defaults 0 0' >> /etc/fstab
  # 下面的命令在当前的系统中启用swapfile，如果内存足够，可以不执行
  swapon /swapfile
  ```

  首先需要安装 GRUB 相关的包。

  如果你不需要支持双系统，则不需要安装 `os-prober`。

  ```zsh
  # 安装GRUB相关的包
  # 如果不需要双系统，可以不安装os-prober
  pacman -S grub efibootmgr os-prober
  ```

  接下来，将 GRUB 相关的 EFI 启动项安装到你的电脑中，并生成 GRUB 配置文件。

  ```zsh
  # bootloader-id可以取一个你喜欢的，也可以不加这个参数，使用默认启动项名称(arch)
  grub-install --target=x86_64-efi --efi-directory=/efi --bootloader-id=archlinux
  # 生成配置
  grub-mkconfig -o /boot/grub/grub.cfg
  ```

  此时，新安装的 Arch Linux 已经可以正常引导。在进入系统前，需要进行最后一步，安装桌面环境。

  现在来看看安装 KDE 需要安装哪些包。

  KDE Plasma 桌面环境：`plasma-meta`/`plasma`(二选一，推荐 `plasma-meta`)

  KDE Plasma (Wayland) (可选)：`plasma-wayland-session`，`egl-wayland`(如要用 Wayland，NVIDIA 显卡用户必须安装)

  KDE 附加软件：`kde-applications`/`kde-applications-meta`(二选一，安装所有 KDE 附加软件)

==如果你想更细的安装 KDE 附加软件组，可以看看 [`kde-applications-meta`](https://archlinux.org/packages/extra/any/kde-applications-meta/) 中的相关依赖。如果确实要这么做，推荐必装下面列出的软件包，可保证 KDE 基础功能：`kde-accessibility-meta`，`kde-graphics-meta`，`kde-multimedia-meta`，`kde-network-meta`，`kde-sdk-meta`，`kde-system-meta`，`kde-utilities-meta`。==

Xorg/X11 相关软件包 (可选)：`xorg`

  KDE 打印机功能：`cups`(需要启用 `cups` 服务才能正常使用)

  对于 VMware 虚拟机：`gtkmm3`(否则宿主机～虚拟机间复制粘贴失效)

  在安装所有 KDE 附加软件或 `kde-pim-meta` 时，其中的 `Akonadi` 组件依赖 MySQL 数据库，默认会给你安装 MariaDB。如果你需要使用其他的 MySQL 包 (比如 MySQL 8.0 Community Edition)，建议在安装所有 KDE 软件或 `kde-pim-meta` 时，同时安装你想要的 MySQL 包。当然，你也可以选择细化安装 KDE 附加软件，不安装 `kde-pim-meta` 包。

  或者，在安装 Akonadi 相关包 (或安装所有 KDE 附加软件) 时，添加参数 `--assume-installed mariadb`。比如：`pacman -S kde-pim-meta --assume-installed mariadb`

  你可能还想要一些中文字体。这里推荐使用 Noto Fonts：`noto-fonts`(基础字体集)，`noto-fonts-cjk`(中日韩字体集，主要是需要这个包)，`noto-fonts-emoji`(表情字体)

  ```zsh
  # KDE软件全部安装的示例命令，同时安装中文字体
  pacman -S plasma-meta kde-applications xorg cups noto-fonts noto-fonts-cjk noto-fonts-emoji gtkmm3
  # 细化安装KDE附加软件的示例命令，同时安装中文字体
  pacman -S plasma-meta kde-accessibility-meta kde-graphics-meta kde-multimedia-meta kde-network-meta kde-sdk-meta \
  kde-system-meta kde-utilities-meta xorg cups noto-fonts noto-fonts-cjk noto-fonts-emoji gtkmm3
  ```

  完成上述包的安装后，启用 `sddm` 显示管理器即可。

  ```zsh
  systemctl enable sddm
  # 如果上面安装了cups服务，记得启用
  systemctl enable cups
  ```

  如果怕等下没浏览器用，可以在进行下一步之前，再安装个 Firefox。

  ```zsh
  pacman -S firefox
  ```

  此时，新安装的 Arch Linux 已经进入了基本可用并且可以引导启动的状态。退出 `chroot` 模式，重启系统。

  ```zsh
  # 退出chroot
  exit
  # 此时已经退出arch-chroot，重启系统。
  reboot
  ```

  当先后出现下面的界面时就代表前面的配置成功。

  ![](https://z1.ax1x.com/2023/01/06/pSAJYfU.png)

  sddm 登录界面。

  ![](https://z1.ax1x.com/2023/01/06/pSAJUl4.png)

  登录后，即可进入 KDE Plasma 桌面环境。

  ![](https://z1.ax1x.com/2023/01/06/pSAJOXj.png)

  如果你喜欢用英文环境，这步可以不看。

  为防止 TTY 乱码，修改 `/etc/locale.conf` 文件，先将全局语言设置为 en\_US。

  ```zsh
  LANG=en_US.UTF-8
  ```

  接下来针对当前用户设置语言和格式。

  如果你使用的是 X11，打开（或新建）`~/.xprofile` 并输入下面的内容。如果你想，可以把这些内容同时写入到 `~/.xinitrc`.

  如果你使用的是 Wayland，则需要将下述内容写入至 `~/.config/environment.d/envvars.conf` 中（如目录不存在则手动新建此目录）。

  ```bash
  export LANG=zh_CN.UTF-8
  export LANGUAGE=zh_CN:en_US
  export LC_ADDRESS=zh_CN.UTF-8
  export LC_CTYPE=zh_CN.UTF-8
  export LC_IDENTIFICATION=zh_CN.UTF-8
  export LC_MEASUREMENT=zh_CN.UTF-8
  export LC_MESSAGES=zh_CN.UTF-8
  export LC_MONETARY=zh_CN.UTF-8
  export LC_NAME=zh_CN.UTF-8
  export LC_NUMERIC=zh_CN.UTF-8
  export LC_PAPER=zh_CN.UTF-8
  export LC_TELEPHONE=zh_CN.UTF-8
  export LC_TIME=zh_CN.UTF-8
  export LC_COLLATE=zh_CN.UTF-8
  ```

  打开设置，选择 _Regional Settings>Regions & Languages>Language_，将简体中文加到语言选项中，并将其优先级调整到最高。

  记得点 Apply。

  ![](data:image/svg+xml;base64,PCEtLUFyZ29uTG9hZGluZy0tPgo8c3ZnIHdpZHRoPSIxIiBoZWlnaHQ9IjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3Ryb2tlPSIjZmZmZmZmMDAiPjxnPjwvZz4KPC9zdmc+)

  接着我们设置一下 sddm 登录界面的语言。

  输入下面命令，进入 systemd 服务编辑界面。不推荐直接修改 sddm 的相关服务文件，否则 sddm 更新时相关更改会被覆盖。

  ```bash
  sudo systemctl edit sddm
  ```

  追加下面的内容，然后保存文件。注意编辑的位置，不要编辑到 `### Lines below this comment will be discarded` 这行下面去。

  ```bash
  [Service]
  Environment=LANG=zh_CN.UTF8
  ```

  ![](data:image/svg+xml;base64,PCEtLUFyZ29uTG9hZGluZy0tPgo8c3ZnIHdpZHRoPSIxIiBoZWlnaHQ9IjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3Ryb2tlPSIjZmZmZmZmMDAiPjxnPjwvZz4KPC9zdmc+)

  如果日后需要还原相关设置，可以输入 `sudo systemctl revert sddm`。

  修改结束后，重启系统，此时系统就会变为全中文环境。

  ![](data:image/svg+xml;base64,PCEtLUFyZ29uTG9hZGluZy0tPgo8c3ZnIHdpZHRoPSIxIiBoZWlnaHQ9IjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3Ryb2tlPSIjZmZmZmZmMDAiPjxnPjwvZz4KPC9zdmc+)

  ![](data:image/svg+xml;base64,PCEtLUFyZ29uTG9hZGluZy0tPgo8c3ZnIHdpZHRoPSIxIiBoZWlnaHQ9IjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3Ryb2tlPSIjZmZmZmZmMDAiPjxnPjwvZz4KPC9zdmc+)

  如果你想直接使用英文环境，那么你可能会发现，中文字体显示的很奇怪 (根据 ArchWiki，实际上这是 Noto Fonts 的日文字体)。

  ![](data:image/svg+xml;base64,PCEtLUFyZ29uTG9hZGluZy0tPgo8c3ZnIHdpZHRoPSIxIiBoZWlnaHQ9IjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3Ryb2tlPSIjZmZmZmZmMDAiPjxnPjwvZz4KPC9zdmc+)

  此时需要调整 fontconfig 的相关文件，使 Noto Fonts 的中文字体优先显示。

  另外，我们同时优化一下 Noto Fonts Emoji 的显示，不做优化的情况下，Konsole 中的相关 emoji 可能会显示不正常 (我说的就是你 minikube)。

  ```bash
  # 将下边的fontconfig文件内容扔到你home目录的~/.config/fontconfig/conf.d目录里
  # 如果该目录不存在则需要手动新建
  vim ~/.config/fontconfig/conf.d/64-language-selector-prefer.conf
  # 可选：你也可以将这个fontconfig文件放到系统全局配置的位置
  # 需要使用root权限进行创建/编辑，因此，创建/编辑下面的文件时需要使用sudo
  sudo vim /etc/fonts/conf.d/64-language-selector-prefer.conf
  # 编辑完成后刷新字体缓存
  fc-cache -fv
  ```

  做完上述步骤建议注销并重新登录一次。

  `64-language-selector-prefer.conf` 的内容：

  ```xml
  <?xml version="1.0"?>
  <fontconfig>
  <alias>
  <family>sans-serif</family>
  <prefer>
  <family>Noto Sans</family>
  <family>Noto Sans CJK SC</family>
  <family>Noto Sans CJK TC</family>
  <family>Noto Sans CJK JP</family>
  <family>Noto Sans CJK KR</family>
  <family>Noto Color Emoji</family>
  <family>Noto Emoji</family>
  </prefer>
  </alias>
  <alias>
  <family>serif</family>
  <prefer>
  <family>Noto Serif</family>
  <family>Noto Serif CJK SC</family>
  <family>Noto Serif CJK TC</family>
  <family>Noto Serif CJK JP</family>
  <family>Noto Serif CJK KR</family>
  <family>Noto Color Emoji</family>
  <family>Noto Emoji</family>
  </prefer>
  </alias>
  <alias>
  <family>monospace</family>
  <prefer>
  <family>Hack</family>
  <family>Noto Sans Mono CJK SC</family>
  <family>Noto Sans Mono CJK TC</family>
  <family>Noto Sans Mono CJK JP</family>
  <family>Noto Sans Mono CJK KR</family>
  <family>Noto Color Emoji</family>
  <family>Noto Emoji</family>
  </prefer>
  </alias>
  </fontconfig>
  ```

  在 KDE 中推荐使用 fcitx5 输入法。

  ```bash
  sudo pacman -S fcitx5 fcitx5-configtool fcitx5-chinese-addons fcitx5-gtk
  ```

  将下面的内容追加到 `/etc/environment` 中：

  ```bash
  INPUT_METHOD=fcitx5
  GTK_IM_MODULE=fcitx5
  QT_IM_MODULE=fcitx5
  XMODIFIERS="@im=fcitx5"
  SDL_IM_MODULE=fcitx
  ```

  注销并重新登录，此时 fcitx 即可使用。

  在 _ 设置 > 语言和区域设置 > 输入法 _ 中添加中文输入法即可。

  ![](data:image/svg+xml;base64,PCEtLUFyZ29uTG9hZGluZy0tPgo8c3ZnIHdpZHRoPSIxIiBoZWlnaHQ9IjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3Ryb2tlPSIjZmZmZmZmMDAiPjxnPjwvZz4KPC9zdmc+)

  如果你想玩 Rime 输入法，也不是不行：

  ```bash
  pacman -S fcitx5-rime rime-pinyin-zhwiki
  ```

  Rime 的配置非常复杂。如果有可能，我也可以开个坑来介绍 Rime 输入法。

  进入 _ 设置 > 显卡与显示器 > 显示器配置 _，修改 _ 全局缩放率 _ 选项。

  ![](data:image/svg+xml;base64,PCEtLUFyZ29uTG9hZGluZy0tPgo8c3ZnIHdpZHRoPSIxIiBoZWlnaHQ9IjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3Ryb2tlPSIjZmZmZmZmMDAiPjxnPjwvZz4KPC9zdmc+)

  如果你觉得 sddm 的登录界面字体太小，可以同时优化一下 sddm 的 HiDPI 设置。

  向 `/etc/sddm.conf` 中追加下面的内容，记得将 96 换成自己的 DPI 缩放数值 (为 96 乘以你的缩放比例，比如 125% 缩放则为 120)。

  ```bash
  [Wayland]
  EnableHiDPI=true
  [X11]
  EnableHiDPI=true
  ServerArguments=-nolisten tcp -dpi 96
  ```

  修改完 HiDPI 设置之后可能需要重新启动系统。

  你可能觉得现在的 sddm 登录界面过于简陋，想修改一下。

  打开 _ 设置 > 开机与关机 > 登录屏幕 (SDDM)_，选择一款你喜欢的登录界面，并且记得应用设置。

  ![](data:image/svg+xml;base64,PCEtLUFyZ29uTG9hZGluZy0tPgo8c3ZnIHdpZHRoPSIxIiBoZWlnaHQ9IjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3Ryb2tlPSIjZmZmZmZmMDAiPjxnPjwvZz4KPC9zdmc+)

  同时你可能还发现 sddm 登录界面不会自动将数字小键盘打开。可以向 `/etc/sddm.conf` 中追加下面的内容，来让 sddm 登录界面默认打开小键盘。

  以及，你可能想调整一下 sddm 的登录鼠标指针。

  ```ini
  [General]
  Numlock=on
  # 如果你想修改sddm登录界面的鼠标指针，加入下面的设置
  [Theme]
  CursorTheme=breeze_cursors
  ```

  重启系统即可。

  AUR (Arch Linux User Repository)，是 Arch Linux 官方源之外的，一个很重要的软件来源。AUR 中的包由用户提供，在官方库找不到的软件包，大部分情况下你总能在 AUR 中找到相应的软件包，比如 Visual Studio Code，Microsft Edge，Google Chrome 等等。_没有找到自己想要的软件包怎么办？你可以尝试自己编写相关的文件，上传到 AUR，分享给其他用户。_

  ![](data:image/svg+xml;base64,PCEtLUFyZ29uTG9hZGluZy0tPgo8c3ZnIHdpZHRoPSIxIiBoZWlnaHQ9IjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3Ryb2tlPSIjZmZmZmZmMDAiPjxnPjwvZz4KPC9zdmc+)

  所有的 AUR 软件包均以软件包构建脚本 (PKGBUILD) 的形式提供，需要你将相关的软件包构建文件和 PKGBUILD 下载到你的 Arch Linux 中，手动构建，并安装。听起来有点麻烦，此时你可能就需要 AUR Helper 来帮忙处理 AUR 中的软件包。

  目前已经有很多现成的 AUR Helper，此处介绍两个 AUR Helper：`yay` 和 `paru`。

  在安装 AUR Helper 之前，我们需要手动将 AUR 上的一个 AUR Helper 软件包下载到本地，并进行安装。

  yay 对应的 AUR 软件包：`yay`(编译构建软件包)，`yay-bin`(通过预编译的二进制文件构建软件包，推荐使用这个)

  paru 对应的 AUR 软件包：`paru`(编译构建软件包)，`paru-bin`(通过预编译的二进制文件构建软件包，推荐使用这个)

  此处以 paru 举例，进行安装。

  ```bash
  # 执行命令前请确保安装了base-devel和git软件包，否则接下来的操作可能失败
  # 请将paru-bin自行替换为自己需要的AUR Helper软件包
  git clone https://aur.archlinux.org/paru-bin.git # 从AUR拉取相关的构建文件
  cd paru-bin
  makepkg -si # 构建软件包，并在构建成功后立刻安装到系统中
  ```

  在任意一个 AUR Helper 安装完成之后，你就能利用这个 AUR Helper 方便的安装 AUR 中的软件。

  需要注意的是，`yay` 和 `paru` 尽量不要在 root 权限下运行。

  ```bash
  # yay和paru的命令用法和pacman很相似。
  # 下面列举的paru用法，与yay和pacman的相关用法基本一致。基本可以认为将paru直接替换成yay或pacman就行。
  # 此处以visual-studio-code-bin，即Visual Studio Code举例。
  # yay和paru均不推荐使用root权限运行！
  # 查询软件包
  paru -Ss visual-studio-code-bin
  # 安装软件包
  paru -S visual studio-code-bin
  # 卸载软件包，并卸载依赖
  paru -Rsn visual-studio-code-bin
  # 全局更新，先执行系统更新，再执行AUR更新
  paru -Syu
  # 清理缓存文件
  paru -Scc
  ```

  _这一段根据博主的实体机 Arch Linux 使用习惯，实时更新。_

  KDE 默认会使用主板蜂鸣器 (下面简称 Beep 音)，在某些场合 (日用感觉有相当一部分地方) 会触发 Beep 音。

  虚拟机还好说，如果是实体机，这个 Beep 音不走耳机，有的时候会非常尴尬。

  在 _ 设置 > 无障碍辅助 > 声音 / 视觉提示 _ 中，将 _ 声音提示 _ 关闭即可解决 Beep 音问题。

  这个快捷键，在部分 Linux 发行版上确实存在。

  打开 _ 设置 > 快捷键 _，选择 _ 添加应用程序 _，将 Konsole 添加进来。添加之后即可使用 Ctrl+Alt+T 打开 Konsole。

  由于从 KDE Plasma 5.25 开始，默认通过一个用户级别 systemd 服务来启动和管理 Plasma 相关服务，而 VMware Tools 用户服务暂时不支持通过这种方式启动所导致。

  目前的一种解决方法是禁用这个默认的用户级别 systemd 服务启动方式，但是不保证后续版本的 KDE Plasma 中该方法依然有效。另外，此方法对 KDE Wayland 无效。

  ```bash
  kwriteconfig5 --file startkderc --group General --key systemdBoot false
  ```

  执行完命令后，注销并重新登录。

  以下是个人提供的一份可供 Arch Linux 安装的软件，可供参考。

  浏览器：`firefox`，`chromium`，`microsoft-edge-stable-bin`AUR，`google-chrome`AUR

  办公：`libreoffice-fresh`，`wps-office`AUR

  聊天：`discord`，`linuxqq`AUR

  代码编辑：`visual-studio-code-bin`AUR

  直播 / 录屏：`obs-studio`

  JDK：`jdk17-openjdk`，`jdk11-openjdk`，`jdk8-openjdk`

  Java 代码构建系统：`maven`，`gradle`

  .NET Core 开发：`dotnet-sdk`，`aspnet-targeting-pack`，`aspnet-runtime`

  邮件处理：`thunderbird`

  远程桌面连接：`remmina`(如果需要 RDP 支持则需要安装 `freerdp`)

  容器管理：`docker`

  笔记本电源管理：`power-profiles-daemon`(需要启用 `power-profiles-daemon` 服务)

  1. 经常对系统进行更新。对整个系统进行更新的命令是 `pacman -Syu`。在更新前，记得查看 Arch Linux 官网，了解有哪些包的更新需要手动干预。如果你有加 Arch Linux 相关的社交群组，可以留意一下其他用户在更新到最新版本后是否有某些包出现了问题。
  2. 避免 “部分更新”，即单独的运行 `pacman -Sy`，否则安装的新包可能会因为库与库之间的兼容性问题而导致一些奇怪错误。另外，在安装新包前一定要更新整个系统，不然 pacman 在下载包时可能出现 404 错误。
  3. 每次 `pacman -Syu` 的时候记得留意一下是否有内核更新。在更新内核之后一定要**立刻**重启系统，不然容易遇到奇奇怪怪的问题（包括但不限于 USB 设备插上了没反应，连接 WiFi 无法认证，文件系统无法识别等），因为更新内核时 pacman 会把旧内核的内核模块文件全部删掉。对于不方便重启的计算机，解决方案是安装 [kernel-modules-hook](https://archlinux.org/packages/extra/any/kernel-modules-hook/) 包。
  4. 记住你对系统做过的一切配置，当你有疑问向他人提问时，一定要说清楚你对系统做过哪些配置。这也是为什么推荐手动安装 Arch Linux 而不是借助第三方安装脚本安装 Arch Linux。
  5. 尽量只安装自己需要的包。
  6. 清理本地缓存的旧版本包的命令是 `pacman -Sc`。如果没有磁盘空间问题，尽量避免使用 `pacman -Scc`。
  此时，你已经得到了一个经过一定优化配置，已经可以使用的 Arch Linux+KDE 桌面环境。恭喜你，完成了初步入门 Arch Linux 的必要步骤。
  开始享受吧！也可以多学习一些相关知识，继续将你的 Arch Linux+KDE 桌面环境打造成你喜欢的样子。
  在编写这篇博文之前，博主也录制了一个相关的 [安装流程视频](https://www.bilibili.com/video/BV1nK411q7SX) (这里可以点击) 可供参考。
  注意，该视频中的部分操作可能和本文的操作有所出入。且由于博主习惯，视频中全程默认使用英文界面。
  (由于 b 站的内嵌播放器现在会自动播放，无法控制，请自行点击上面的链接观看)
