---
created: 2024-01-06T12:00:00
source: https://blog.csdn.net/yjy420/article/details/132305356
type: archive-web
modified: 2025-01-15T11:38:16
---

### 省流版总结

  凡是使用了命令 `nvidia docker` 或者在 docker 中引入了 `--runtime=nvidia` 参数的都是过时教程，最新方法只需要下载 `nvidia-container-toolkits`，在 docker 中引入 `--gpus` 参数即可。

### [nvidia](https://so.csdn.net/so/search?q=nvidia&spm=1001.2101.3001.7020) docker

  nvidia docker 是 NVIDIA 第一代支持 docker 容器内使用 [GPU](https://so.csdn.net/so/search?q=GPU&spm=1001.2101.3001.7020) 资源的项目。运行时用 `nvidia-docker` 命令。

  根据 nvidia docker 在 [github](https://github.com/NVIDIA/nvidia-docker) 上的描述，已经不再使用了。

  > The nvidia-docker wrapper script that was included in this repository is no longer included in the package and a configuration specific to the target container engine (e.g. Docker, Containerd, Cri-o, or Podman) is suggested instead.

### nvidia docker2

  nvidia docker2 是 NVIDIA 第二代支持 docker 容器内使用 GPU 资源的项目。运行时用 `nvidia-docker` 命令，且需要指定参数 `--runtime=nvidia`.

  根据 [github wiki](https://github.com/NVIDIA/nvidia-docker/wiki/Advanced-topics#backward-compatibility) 的描述，一代和二代之间有如下兼容性。

  > Backward compatibility To help transitioning code from 1.0 to 2.0, a bash script is provided in /usr/bin/nvidia-docker for backward compatibility. It will automatically inject the --runtime=nvidia argument and convert NV\_GPU to NVIDIA\_VISIBLE\_DEVICES.
  也就是说，在二代中，既可以使用 `nvidia docker` 命令，这会自动引入参数 `--runtime=nvidia` 也可以使用 `docker` 命令，手动指定参数 `--runtime=nvidia`
  如 [帖子](https://stackoverflow.com/questions/50462153/nvidia-docker-run-vs-docker-run-runtime-nvidia) 总结：
  > docker run --runtime=nvidia is only available since nvidia-docker v2.
  > Both commands are equivalent with nvidia-docker v2, the former is a script provided for backward compatibility with nvidia-docker v1.

### nvidia-container-toolkits

  根据 [github](https://github.com/NVIDIA/nvidia-docker) 这是最新的支持方案，如 [帖子](https://stackoverflow.com/questions/52865988/nvidia-docker-unknown-runtime-specified-nvidia?rq=3) 描述，nvidia docker2 被 Nvidia container toolkits 取代，无需指定 `--runtime` 参数，只需要传递 `--gpus` 参数
