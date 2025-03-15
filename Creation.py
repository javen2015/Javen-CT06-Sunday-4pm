# 2025-03-15 05:57:14.586Z: Host information
# 2025-03-15 05:57:14.587Z: ----------------
# 2025-03-15 05:57:14.587Z: OS: Ubuntu 22.04.5 LTS (stable release)
# 2025-03-15 05:57:14.587Z: Image details: https://github.com/github/codespaces-host-images/blob/main/README.md
# 2025-03-15 05:57:14.587Z: ----------------

# =================================================================================
# 2025-03-15 05:57:14.590Z: Configuration starting...
# 2025-03-15 05:57:14.612Z: Cloning...
# 2025-03-15 05:57:15.630Z: Using image: mcr.microsoft.com/devcontainers/universal

# =================================================================================
# 2025-03-15 05:57:15.756Z: Creating container...
# 2025-03-15 05:57:15.807Z: $ devcontainer up --id-label Type=codespaces --workspace-folder /var/lib/docker/codespacemount/workspace/PythonThinker2-CT07-StudentsCopy-v2 --mount type=bind,source=/.codespaces/agent/mount/cache,target=/vscode --user-data-folder /var/lib/docker/codespacemount/.persistedshare --container-data-folder .vscode-remote/data/Machine --container-system-data-folder /var/vscode-remote --log-level trace --log-format json --update-remote-user-uid-default never --mount-workspace-git-root false --omit-config-remote-env-from-metadata --skip-non-blocking-commands --skip-post-create --config "/var/lib/docker/codespacemount/workspace/PythonThinker2-CT07-StudentsCopy-v2/.devcontainer/devcontainer.json" --override-config /root/.codespaces/shared/merged_devcontainer.json --default-user-env-probe loginInteractiveShell --container-session-data-folder /workspaces/.codespaces/.persistedshare/devcontainers-cli/cache --secrets-file /root/.codespaces/shared/user-secrets-envs.json
# 2025-03-15 05:57:15.990Z: @devcontainers/cli 0.68.0. Node.js v18.20.6. linux 6.8.0-1021-azure x64.
# 2025-03-15 05:57:16.116Z: Resolving Feature dependencies for 'ghcr.io/devcontainers/features/desktop-lite:1'...
# 2025-03-15 05:57:17.935Z: Soft-dependency 'ghcr.io/devcontainers/features/common-utils' is not required.  Removing from installation order...
# 2025-03-15 05:57:18.617Z: Files to omit: ''
# 2025-03-15 05:57:18.634Z: $2 --build-arg _DEV_CONTAINERS_IMAGE_USER=root --build-arg _DEV_CONTAINERS_FEATURE_CONTENT_SOURCE=dev_container_feature_content_temp --target dev_containers_target_stage -f /tmp/devcontainercli-root/container-features/0.68.0-1742018236108/Dockerfile.extended -t vsc-pythonthinker2-ct07-studentscopy-v2-f0434683cd236a5afb1752e3ab9c89d8f50b4d6a4563b7ee4af98e948610d37e-features /var/lib/docker/codespacemount/.persistedshare/empty-folder
# 2025-03-15 05:57:19.078Z: #0 building with "default" instance using docker driver

# #1 [internal] load .dockerignore
# 2025-03-15 05:57:19.078Z: #1 transferring context: 2B done
# #1 DONE 0.0s

# #2 [internal] load build definition from Dockerfile.extended
# #2 transferring dockerfile: 5.95kB done
# #2 DONE 0.0s

# #3 resolve image config for docker.io/docker/dockerfile:1.4
# 2025-03-15 05:57:19.815Z: #3 ...

# #4 [auth] docker/dockerfile:pull token for registry-1.docker.io
# #4 DONE 0.0s
# 2025-03-15 05:57:19.964Z: 
# #3 resolve image config for docker.io/docker/dockerfile:1.4
# 2025-03-15 05:57:21.599Z: #3 DONE 2.7s
# 2025-03-15 05:57:21.702Z: 
# #5 docker-image://docker.io/docker/dockerfile:1.4@sha256:9ba7531bd80fb0a858632727cf7a112fbfd19b17e94c4e84ced81e24ef1a0dbc
# #5 resolve docker.io/docker/dockerfile:1.4@sha256:9ba7531bd80fb0a858632727cf7a112fbfd19b17e94c4e84ced81e24ef1a0dbc done
# #5 sha256:1e8a16826fd1c80a63fa6817a9c7284c94e40cded14a9b0d0d3722356efa47bd 2.37kB / 2.37kB done
# #5 sha256:1328b32c40fca9bcf9d70d8eccb72eb873d1124d72dadce04db8badbe7b08546 0B / 9.94MB 0.1s
# #5 sha256:9ba7531bd80fb0a858632727cf7a112fbfd19b17e94c4e84ced81e24ef1a0dbc 2.00kB / 2.00kB done
# #5 sha256:ad87fb03593d1b71f9a1cfc1406c4aafcb253b1dabebf569768d6e6166836f34 528B / 528B done
# 2025-03-15 05:57:21.903Z: #5 sha256:1328b32c40fca9bcf9d70d8eccb72eb873d1124d72dadce04db8badbe7b08546 7.34MB / 9.94MB 0.3s
# 2025-03-15 05:57:22.055Z: #5 sha256:1328b32c40fca9bcf9d70d8eccb72eb873d1124d72dadce04db8badbe7b08546 9.94MB / 9.94MB 0.4s
# #5 extracting sha256:1328b32c40fca9bcf9d70d8eccb72eb873d1124d72dadce04db8badbe7b08546
# 2025-03-15 05:57:22.155Z: #5 sha256:1328b32c40fca9bcf9d70d8eccb72eb873d1124d72dadce04db8badbe7b08546 9.94MB / 9.94MB 0.4s done
# 2025-03-15 05:57:22.329Z: #5 extracting sha256:1328b32c40fca9bcf9d70d8eccb72eb873d1124d72dadce04db8badbe7b08546 0.1s done2025-03-15 05:57:22.329Z: 
# #5 DONE 0.6s
# 2025-03-15 05:57:22.495Z: 
# #6 [internal] load metadata for mcr.microsoft.com/devcontainers/universal:2
# #6 DONE 0.0s

# #7 [context dev_containers_feature_content_source] load .dockerignore
# #7 transferring dev_containers_feature_content_source: 2B done
# #7 DONE 0.0s
# 2025-03-15 05:57:22.797Z: 
# #8 [context dev_containers_feature_content_source] load from client
# #8 transferring dev_containers_feature_content_source: 64.59kB done
# #8 DONE 0.0s

# #9 [dev_containers_feature_content_normalize 1/3] FROM mcr.microsoft.com/devcontainers/universal:2
# 2025-03-15 05:57:22.909Z: #9 DONE 0.3s2025-03-15 05:57:22.909Z: 
# 2025-03-15 05:57:23.127Z: 
# 2025-03-15 05:57:23.127Z: #10 [dev_containers_feature_content_normalize 2/3] COPY --from=dev_containers_feature_content_source devcontainer-features.builtin.env /tmp/build-features/
# #10 DONE 0.1s

# #11 [dev_containers_feature_content_normalize 3/3] RUN chmod -R 0755 /tmp/build-features/
# 2025-03-15 05:57:23.396Z: #11 ...2025-03-15 05:57:23.397Z: 

# #12 [dev_containers_target_stage 2/5] RUN mkdir -p /tmp/dev-container-features
# #12 DONE 0.5s
# 2025-03-15 05:57:23.498Z: 
# #11 [dev_containers_feature_content_normalize 3/3] RUN chmod -R 0755 /tmp/build-features/
# 2025-03-15 05:57:23.499Z: #11 DONE 0.4s

# #13 [dev_containers_target_stage 3/5] COPY --from=dev_containers_feature_content_normalize /tmp/build-features/ /tmp/dev-container-features
# 2025-03-15 05:57:23.687Z: #13 DONE 0.0s

# #14 [dev_containers_target_stage 4/5] RUN echo "_CONTAINER_USER_HOME=$( (command -v getent >/dev/null 2>&1 && getent passwd 'codespace' || grep -E '^codespace|^[^:]*:[^:]*:codespace:' /etc/passwd || ********) | cut -d: -f6)" >> /tmp/dev-container-features/devcontainer-features.builtin.env && echo "_REMOTE_USER_HOME=$( (command -v getent >/dev/null 2>&1 && getent passwd 'codespace' || grep -E '^codespace|^[^:]*:[^:]*:codespace:' /etc/passwd || ********) | cut -d: -f6)" >> /tmp/dev-container-features/devcontainer-features.builtin.env
# 2025-03-15 05:57:23.724Z: #14 DONE 0.2s2025-03-15 05:57:23.726Z: 
# 2025-03-15 05:57:23.876Z: 
# #15 [dev_containers_target_stage 5/5] RUN --mount=type=bind,from=dev_containers_feature_content_source,source=desktop-lite_0,target=/tmp/build-features-src/desktop-lite_0     cp -ar /tmp/build-features-src/desktop-lite_0 /tmp/dev-container-features  && chmod -R 0755 /tmp/dev-container-features/desktop-lite_0  && cd /tmp/dev-container-features/desktop-lite_0  && chmod +x ./devcontainer-features-install.sh  && ./devcontainer-features-install.sh  && rm -rf /tmp/dev-container-features/desktop-lite_0
# 2025-03-15 05:57:23.970Z: #15 0.254 ===========================================================================
# #15 0.254 Feature       : Light-weight Desktop
# 2025-03-15 05:57:24.158Z: #15 0.255 Description   : Adds a lightweight Fluxbox based desktop to the container that can be accessed using a VNC viewer or the web. GUI-based commands executed from the built-in VS code terminal will open on the desktop automatically.
# #15 0.255 Id            : ghcr.io/devcontainers/features/desktop-lite
# #15 0.255 Version       : 1.2.5
# #15 0.255 Documentation : ********/devcontainers/features/tree/main/src/desktop-lite
# #15 0.255 Options       :
# #15 0.255     VERSION="latest"
# #15 0.255     NOVNCVERSION="1.2.0"
# #15 0.255     PASSWORD="vscode"
# #15 0.255     WEBPORT="6080"
# #15 0.255     VNCPORT="5901"
# #15 0.255 ===========================================================================
# #15 0.290 find: ‘/var/lib/apt/lists/*’: No such file or directory
# #15 0.292 Running apt-get update...
# 2025-03-15 05:57:24.332Z: #15 0.617 Get:1 https://packages.microsoft.com/repos/microsoft-ubuntu-focal-prod focal InRelease [3631 B]
# 2025-03-15 05:57:24.435Z: #15 0.667 Get:2 https://dl.yarnpkg.com/debian stable InRelease [17.1 kB]2025-03-15 05:57:24.435Z: 
# #15 0.674 Get:3 https://repo.anaconda.com/pkgs/misc/debrepo/conda stable InRelease [3961 B]
# #15 0.701 Get:4 https://packages.microsoft.com/repos/microsoft-ubuntu-focal-prod focal/main amd64 Packages [338 kB]
# #15 0.719 Get:5 https://packages.microsoft.com/repos/microsoft-ubuntu-focal-prod focal/main all Packages [2938 B]
# 2025-03-15 05:57:24.566Z: #15 0.782 Get:6 https://dl.yarnpkg.com/debian stable/main all Packages [11.8 kB]
# #15 0.851 Get:7 https://repo.anaconda.com/pkgs/misc/debrepo/conda stable/main amd64 Packages [4557 B]
# 2025-03-15 05:57:24.867Z: #15 1.152 Get:8 https://dl.yarnpkg.com/debian stable/main amd64 Packages [11.8 kB]
# 2025-03-15 05:57:24.978Z: #15 1.263 Get:9 http://security.ubuntu.com/ubuntu focal-security InRelease [128 kB]2025-03-15 05:57:24.979Z: 
# 2025-03-15 05:57:25.141Z: #15 1.275 Get:10 http://archive.ubuntu.com/ubuntu focal InRelease [265 kB]
# 2025-03-15 05:57:25.202Z: #15 1.487 Err:11 https://packagecloud.io/github/git-lfs/ubuntu focal InRelease
# #15 1.487   403  Forbidden [IP: 3.165.92.186 443]
# 2025-03-15 05:57:25.878Z: #15 2.162 Get:12 http://archive.ubuntu.com/ubuntu focal-updates InRelease [128 kB]
# 2025-03-15 05:57:26.090Z: #15 2.375 Get:13 http://archive.ubuntu.com/ubuntu focal-backports InRelease [128 kB]
# 2025-03-15 05:57:26.303Z: #15 2.437 Get:14 http://security.ubuntu.com/ubuntu focal-security/multiverse amd64 Packages [42.0 kB]
# 2025-03-15 05:57:26.304Z: #15 2.590 Get:15 http://archive.ubuntu.com/ubuntu focal/universe amd64 Packages [11.3 MB]
# 2025-03-15 05:57:26.437Z: #15 2.722 Get:16 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages [4269 kB]
# 2025-03-15 05:57:27.260Z: #15 3.541 Get:17 http://archive.ubuntu.com/ubuntu focal/restricted amd64 Packages [33.4 kB]2025-03-15 05:57:27.262Z: 
# 2025-03-15 05:57:27.262Z: #15 3.541 Get:18 http://archive.ubuntu.com/ubuntu focal/main amd64 Packages [1275 kB]
# 2025-03-15 05:57:27.455Z: #15 3.581 Get:19 http://archive.ubuntu.com/ubuntu focal/multiverse amd64 Packages [177 kB]
# #15 3.585 Get:20 http://archive.ubuntu.com/ubuntu focal-updates/multiverse amd64 Packages [45.5 kB]2025-03-15 05:57:27.455Z: 
# #15 3.587 Get:21 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages [4748 kB]
# 2025-03-15 05:57:27.481Z: #15 3.764 Get:22 http://archive.ubuntu.com/ubuntu focal-updates/universe amd64 Packages [1593 kB]
# 2025-03-15 05:57:27.671Z: #15 3.826 Get:23 http://archive.ubuntu.com/ubuntu focal-updates/restricted amd64 Packages [4638 kB]
# 2025-03-15 05:57:27.671Z: #15 3.951 Get:24 http://security.ubuntu.com/ubuntu focal-security/restricted amd64 Packages [4441 kB]
# 2025-03-15 05:57:27.870Z: #15 3.999 Get:25 http://archive.ubuntu.com/ubuntu focal-backports/universe amd64 Packages [28.6 kB]2025-03-15 05:57:27.871Z: 
# #15 4.004 Get:26 http://archive.ubuntu.com/ubuntu focal-backports/main amd64 Packages [55.2 kB]
# 2025-03-15 05:57:27.907Z: #15 4.191 Get:27 http://security.ubuntu.com/ubuntu focal-security/universe amd64 Packages [1301 kB]2025-03-15 05:57:27.908Z: 
# 2025-03-15 05:57:29.047Z: #15 5.331 Reading package lists...2025-03-15 05:57:30.028Z: 
# 2025-03-15 05:57:30.199Z: #15 6.332 E: Failed to fetch https://packagecloud.io/github/git-lfs/ubuntu/dists/focal/InRelease  403  Forbidden [IP: 3.165.92.186 443]
# #15 6.332 E: The repository 'https://packagecloud.io/github/git-lfs/ubuntu focal InRelease' is not signed.
# 2025-03-15 05:57:30.200Z: #15 6.333 ERROR: Feature "Light-weight Desktop" (ghcr.io/devcontainers/features/desktop-lite) failed to install! Look at the documentation at ********/devcontainers/features/tree/main/src/desktop-lite for help troubleshooting this error.
# 2025-03-15 05:57:30.727Z: #15 ERROR: process "/bin/sh -c cp -ar /tmp/build-features-src/desktop-lite_0 /tmp/dev-container-features  && chmod -R 0755 /tmp/dev-container-features/desktop-lite_0  && cd /tmp/dev-container-features/desktop-lite_0  && chmod +x ./devcontainer-features-install.sh  && ./devcontainer-features-install.sh  && rm -rf /tmp/dev-container-features/desktop-lite_0" did not complete successfully: exit code: 100
# 2025-03-15 05:57:30.753Z: ------
#  > [dev_containers_target_stage 5/5] RUN --mount=type=bind,from=dev_containers_feature_content_source,source=desktop-lite_0,target=/tmp/build-features-src/desktop-lite_0     cp -ar /tmp/build-features-src/desktop-lite_0 /tmp/dev-container-features  && chmod -R 0755 /tmp/dev-container-features/desktop-lite_0  && cd /tmp/dev-container-features/desktop-lite_0  && chmod +x ./devcontainer-features-install.sh  && ./devcontainer-features-install.sh  && rm -rf /tmp/dev-container-features/desktop-lite_0:
# 3.764 Get:22 http://archive.ubuntu.com/ubuntu focal-updates/universe amd64 Packages [1593 kB]
# 3.826 Get:23 http://archive.ubuntu.com/ubuntu focal-updates/restricted amd64 Packages [4638 kB]
# 3.951 Get:24 http://security.ubuntu.com/ubuntu focal-security/restricted amd64 Packages [4441 kB]
# 3.999 Get:25 http://archive.ubuntu.com/ubuntu focal-backports/universe amd64 Packages [28.6 kB]
# 4.004 Get:26 http://archive.ubuntu.com/ubuntu focal-backports/main amd64 Packages [55.2 kB]
# 4.191 Get:27 http://security.ubuntu.com/ubuntu focal-security/universe amd64 Packages [1301 kB]

# 6.332 E: Failed to fetch https://packagecloud.io/github/git-lfs/ubuntu/dists/focal/InRelease  403  Forbidden [IP: 3.165.92.186 443]
# 6.332 E: The repository 'https://packagecloud.io/github/git-lfs/ubuntu focal InRelease' is not signed.
# 6.333 ERROR: Feature "Light-weight Desktop" (ghcr.io/devcontainers/features/desktop-lite) failed to install! Look at the documentation at ********/devcontainers/features/tree/main/src/desktop-lite for help troubleshooting this error.
# ------
# 2025-03-15 05:57:30.755Z: Dockerfile.extended:24
# --------------------
#   23 |     ENV DISPLAY=":1"
# 2025-03-15 05:57:30.757Z:   24 | >>> RUN --mount=type=bind,from=dev_containers_feature_content_source,source=desktop-lite_0,target=/tmp/build-features-src/desktop-lite_0 \
#   25 | >>>     cp -ar /tmp/build-features-src/desktop-lite_0 /tmp/dev-container-features \
#   26 | >>>  && chmod -R 0755 /tmp/dev-container-features/desktop-lite_0 \
#   27 | >>>  && cd /tmp/dev-container-features/desktop-lite_0 \
#   28 | >>>  && chmod +x ./devcontainer-features-install.sh \
#   29 | >>>  && ./devcontainer-features-install.sh \2025-03-15 05:57:30.757Z: 
#   30 | >>>  && rm -rf /tmp/dev-container-features/desktop-lite_0
#   31 |     
# --------------------
# ERROR: failed to solve: process "/bin/sh -c cp -ar /tmp/build-features-src/desktop-lite_0 /tmp/dev-container-features  && chmod -R 0755 /tmp/dev-container-features/desktop-lite_0  && cd /tmp/dev-container-features/desktop-lite_0  && chmod +x ./devcontainer-features-install.sh  && ./devcontainer-features-install.sh  && rm -rf /tmp/dev-container-features/desktop-lite_0" did not complete successfully: exit code: 100
# 2025-03-15 05:57:30.782Z: Stop: Run: docker buildx build --load --build-context dev_containers_feature_content_source=/tmp/devcontainercli-root/container-features/0.68.0-1742018236108 --build-arg _DEV_CONTAINERS_BASE_IMAGE=mcr.microsoft.com/devcontainers/universal:2 --build-arg _DEV_CONTAINERS_IMAGE_USER=root --build-arg _DEV_CONTAINERS_FEATURE_CONTENT_SOURCE=dev_container_feature_content_temp --target dev_containers_target_stage -f /tmp/devcontainercli-root/container-features/0.68.0-1742018236108/Dockerfile.extended -t vsc-pythonthinker2-ct07-studentscopy-v2-f0434683cd236a5afb1752e3ab9c89d8f50b4d6a4563b7ee4af98e948610d37e-features /var/lib/docker/codespacemount/.persistedshare/empty-folder
# 2025-03-15 05:57:30.786Z: Error: Command failed: docker buildx build --load --build-context dev_containers_feature_content_source=/tmp/devcontainercli-root/container-features/0.68.0-1742018236108 --build-arg _DEV_CONTAINERS_BASE_IMAGE=mcr.microsoft.com/devcontainers/universal:2 --build-arg _DEV_CONTAINERS_IMAGE_USER=root --build-arg _DEV_CONTAINERS_FEATURE_CONTENT_SOURCE=dev_container_feature_content_temp --target dev_containers_target_stage -f /tmp/devcontainercli-root/container-features/0.68.0-1742018236108/Dockerfile.extended -t vsc-pythonthinker2-ct07-studentscopy-v2-f0434683cd236a5afb1752e3ab9c89d8f50b4d6a4563b7ee4af98e948610d37e-features /var/lib/docker/codespacemount/.persistedshare/empty-folder
# 2025-03-15 05:57:30.787Z: {"outcome":"error","message":"Command failed: docker buildx build --load --build-context dev_containers_feature_content_source=/tmp/devcontainercli-root/container-features/0.68.0-1742018236108 --build-arg _DEV_CONTAINERS_BASE_IMAGE=mcr.microsoft.com/devcontainers/universal:2 --build-arg _DEV_CONTAINERS_IMAGE_USER=root --build-arg _DEV_CONTAINERS_FEATURE_CONTENT_SOURCE=dev_container_feature_content_temp --target dev_containers_target_stage -f /tmp/devcontainercli-root/container-features/0.68.0-1742018236108/Dockerfile.extended -t vsc-pythonthinker2-ct07-studentscopy-v2-f0434683cd236a5afb1752e3ab9c89d8f50b4d6a4563b7ee4af98e948610d37e-features /var/lib/docker/codespacemount/.persistedshare/empty-folder","description":"An error occurred setting up the container."}
# 2025-03-15 05:57:30.788Z:     at wtA (/.codespaces/agent/bin/node_modules/@devcontainers/cli/dist/spec-node/devContainersSpecCLI.js:465:1260)
# 2025-03-15 05:57:30.788Z:     at NH (/.codespaces/agent/bin/node_modules/@devcontainers/cli/dist/spec-node/devContainersSpecCLI.js:465:1002)
# 2025-03-15 05:57:30.792Z:     at process.processTicksAndRejections (node:internal/process/task_queues:95:5)
# 2025-03-15 05:57:30.795Z:     at async YtA (/.codespaces/agent/bin/node_modules/@devcontainers/cli/dist/spec-node/devContainersSpecCLI.js:482:3771)
# 2025-03-15 05:57:30.795Z:     at async eB (/.codespaces/agent/bin/node_modules/@devcontainers/cli/dist/spec-node/devContainersSpecCLI.js:482:4886)
# 2025-03-15 05:57:30.795Z:     at async prA (/.codespaces/agent/bin/node_modules/@devcontainers/cli/dist/spec-node/devContainersSpecCLI.js:663:200)
# 2025-03-15 05:57:30.797Z:     at async drA (/.codespaces/agent/bin/node_modules/@devcontainers/cli/dist/spec-node/devContainersSpecCLI.js:662:14706)
# 2025-03-15 05:57:30.805Z: devcontainer process exited with exit code 1

# ====================================== ERROR ====================================
# 2025-03-15 05:57:30.810Z: Failed to create container.
# =================================================================================
# 2025-03-15 05:57:30.810Z: Error: Command failed: docker buildx build --load --build-context dev_containers_feature_content_source=/tmp/devcontainercli-root/container-features/0.68.0-1742018236108 --build-arg _DEV_CONTAINERS_BASE_IMAGE=mcr.microsoft.com/devcontainers/universal:2 --build-arg _DEV_CONTAINERS_IMAGE_USER=root --build-arg _DEV_CONTAINERS_FEATURE_CONTENT_SOURCE=dev_container_feature_content_temp --target dev_containers_target_stage -f /tmp/devcontainercli-root/container-features/0.68.0-1742018236108/Dockerfile.extended -t vsc-pythonthinker2-ct07-studentscopy-v2-f0434683cd236a5afb1752e3ab9c89d8f50b4d6a4563b7ee4af98e948610d37e-features /var/lib/docker/codespacemount/.persistedshare/empty-folder
# 2025-03-15 05:57:30.814Z: Error code: 1302 (UnifiedContainersErrorFatalCreatingContainer)

# ====================================== ERROR ====================================
# 2025-03-15 05:57:30.826Z: Container creation failed.
# =================================================================================
# 2025-03-15 05:57:30.837Z: 

# ===================================== WARNING ===================================
# 2025-03-15 05:57:30.839Z: Creating recovery container.
# =================================================================================

# =================================================================================
# 2025-03-15 05:58:55.106Z: Creating container...
# 2025-03-15 05:58:55.132Z: $ devcontainer up --id-label Type=codespaces --workspace-folder /var/lib/docker/codespacemount/workspace/PythonThinker2-CT07-StudentsCopy-v2 --mount type=bind,source=/.codespaces/agent/mount/cache,target=/vscode --user-data-folder /var/lib/docker/codespacemount/.persistedshare --container-data-folder .vscode-remote/data/Machine --container-system-data-folder /var/vscode-remote --log-level trace --log-format json --update-remote-user-uid-default never --mount-workspace-git-root false --omit-config-remote-env-from-metadata --skip-non-blocking-commands --skip-post-create --config "/var/lib/docker/codespacemount/workspace/PythonThinker2-CT07-StudentsCopy-v2/.devcontainer/devcontainer.json" --override-config /root/.codespaces/shared/merged_devcontainer.json --default-user-env-probe loginInteractiveShell --container-session-data-folder /workspaces/.codespaces/.persistedshare/devcontainers-cli/cache --secrets-file /root/.codespaces/shared/user-secrets-envs.json
# 2025-03-15 05:58:55.323Z: @devcontainers/cli 0.68.0. Node.js v18.20.6. linux 6.8.0-1021-azure x64.
# 2025-03-15 05:58:55.696Z: $alpine -c echo Container started
# 2025-03-15 05:58:55.715Z: Unable to find image 'mcr.microsoft.com/devcontainers/base:alpine' locally2025-03-15 05:58:55.717Z: 
# 2025-03-15 05:58:55.815Z: alpine: Pulling from devcontainers/base
# 2025-03-15 05:58:55.849Z: 
# [1A[2K
# da9db072f522: Pulling fs layer 
# [1B
# [1A[2K
# 3cdff9e33f37: Pulling fs layer 
# [1B
# [1A[2K
# 87dffdaee0b6: Pulling fs layer 
# [1B
# [1A[2K
# 2025-03-15 05:58:55.852Z: 3f72e2f1b3f3: Pulling fs layer 
# [1B
# [1A[2K
# 1ac829ce5af3: Pulling fs layer 
# [1B
# [1A[2K
# 2a15ab263bdf: Pulling fs layer 
# [1B
# [1A[2K
# a9bdcaa5c876: Pulling fs layer 
# [1B[3A[2K
# 1ac829ce5af3: Waiting 
# [3B[2A2025-03-15 05:58:55.853Z: [2K
# 2a15ab263bdf: Waiting 
# [2B[1A[2K
# a9bdcaa5c876: Waiting 
# [1B[4A[2K2025-03-15 05:58:55.854Z: 
# 3f72e2f1b3f3: Waiting 
# [4B2025-03-15 05:58:55.907Z: [7A2025-03-15 05:58:55.907Z: [2K
# da9db072f522: Downloading  48.35kB/3.624MB
# [7B2025-03-15 05:58:55.922Z: [6A[2K2025-03-15 05:58:55.923Z: 
# 3cdff9e33f37: Downloading     410B/410B
# [6B[6A[2K
# 3cdff9e33f37: Verifying Checksum 
# [6B[6A[2K
# 3cdff9e33f37: Download complete 
# [6B[7A[2K
# da9db072f522: Downloading  3.624MB/3.624MB
# [7B[7A[2K
# da9db072f522: Verifying Checksum 
# [7B[7A[2K
# da9db072f522: Download complete 
# [7B2025-03-15 05:58:55.929Z: [5A[2K2025-03-15 05:58:55.930Z: 
# 87dffdaee0b6: Downloading     135B/135B
# [5B[5A[2K
# 87dffdaee0b6: Verifying Checksum 
# [5B[5A[2K
# 87dffdaee0b6: Download complete 
# [5B2025-03-15 05:58:55.932Z: [7A[2K
# da9db072f522: Extracting  65.54kB/3.624MB
# 2025-03-15 05:58:55.932Z: [7B2025-03-15 05:58:55.980Z: [3A[2K
# 1ac829ce5af3: Downloading     235B/235B
# [3B2025-03-15 05:58:55.981Z: [3A[2K
# 1ac829ce5af3: Verifying Checksum 
# [3B[3A[2K2025-03-15 05:58:55.981Z: 
# 1ac829ce5af3: Download complete 
# [3B2025-03-15 05:58:56.005Z: [4A[2K
# 3f72e2f1b3f3: Downloading     223B/223B
# [4B[4A[2K
# 3f72e2f1b3f3: Verifying Checksum 
# [4B[4A[2K
# 3f72e2f1b3f3: Download complete 
# [4B2025-03-15 05:58:56.015Z: [2A[2K2025-03-15 05:58:56.015Z: 
# 2a15ab263bdf: Downloading  538.9kB/230.6MB
# 2025-03-15 05:58:56.015Z: [2B2025-03-15 05:58:56.065Z: [7A[2K
# da9db072f522: Extracting  262.1kB/3.624MB
# [7B2025-03-15 05:58:56.072Z: [1A2025-03-15 05:58:56.072Z: [2K
# a9bdcaa5c876: Downloading  440.6kB/43.41MB
# [1B2025-03-15 05:58:56.114Z: [2A[2K
# 2a15ab263bdf: 2025-03-15 05:58:56.115Z: Downloading  23.23MB/230.6MB
# [2B2025-03-15 05:58:56.167Z: [7A2025-03-15 05:58:56.168Z: [2K
# da9db072f522: Extracting    852kB/3.624MB
# [7B2025-03-15 05:58:56.189Z: [1A[2K
# a9bdcaa5c876: Downloading  23.45MB/43.41MB
# [1B2025-03-15 05:58:56.217Z: [2A[2K
# 2025-03-15 05:58:56.218Z: 2a15ab263bdf: Downloading  42.16MB/230.6MB
# [2B2025-03-15 05:58:56.261Z: [7A[2K2025-03-15 05:58:56.263Z: 
# da9db072f522: Extracting  2.032MB/3.624MB
# [7B2025-03-15 05:58:56.271Z: [1A2025-03-15 05:58:56.271Z: [2K2025-03-15 05:58:56.271Z: 
# 2025-03-15 05:58:56.271Z: a9bdcaa5c876: Verifying Checksum 
# [1B[1A[2K
# a9bdcaa5c876: Download complete 
# [1B2025-03-15 05:58:56.318Z: [7A[2K
# da9db072f522: Extracting  3.624MB/3.624MB
# [7B2025-03-15 05:58:56.319Z: [2A[2K2025-03-15 05:58:56.319Z: 
# 2a15ab263bdf: Downloading   65.4MB/230.6MB
# [2B2025-03-15 05:58:56.386Z: [7A[2K
# da9db072f522: Pull complete 
# 2025-03-15 05:58:56.389Z: [7B2025-03-15 05:58:56.395Z: [6A[2K
# 3cdff9e33f37: Extracting     410B/410B
# [6B[6A[2K
# 3cdff9e33f37: Extracting     410B/410B
# [6B2025-03-15 05:58:56.426Z: [2A[2K
# 2a15ab263bdf: Downloading  88.11MB/230.6MB
# [2B2025-03-15 05:58:56.525Z: [2A[2K
# 2a15ab263bdf: Downloading  104.9MB/230.6MB
# [2B2025-03-15 05:58:56.632Z: [2A[2K
# 2a15ab263bdf: Downloading    120MB/230.6MB
# [2B2025-03-15 05:58:56.733Z: [2A[2K2025-03-15 05:58:56.750Z: 
# 2a15ab263bdf: Downloading  128.1MB/230.6MB
# [2B2025-03-15 05:58:56.837Z: [2A[2K
# 2a15ab263bdf: Downloading  137.3MB/230.6MB
# [2B2025-03-15 05:58:56.935Z: [2A[2K2025-03-15 05:58:56.938Z: 
# 2a15ab263bdf: Downloading  155.7MB/230.6MB
# [2B2025-03-15 05:58:57.035Z: [2A[2K
# 2a15ab263bdf: 2025-03-15 05:58:57.035Z: Downloading  176.8MB/230.6MB
# [2B2025-03-15 05:58:57.135Z: [2A[2K
# 2a15ab263bdf: Downloading  200.6MB/230.6MB
# 2025-03-15 05:58:57.135Z: [2B2025-03-15 05:58:57.236Z: [2A[2K
# 2a15ab263bdf: Downloading  223.8MB/230.6MB
# [2B2025-03-15 05:58:57.268Z: [2A[2K
# 2025-03-15 05:58:57.269Z: 2a15ab263bdf: Verifying Checksum 
# [2B[2A[2K
# 2a15ab263bdf: Download complete 
# [2B2025-03-15 05:58:59.539Z: [6A[2K
# 3cdff9e33f37: Pull complete 
# [6B2025-03-15 05:58:59.543Z: [5A[2K
# 87dffdaee0b6: Extracting     135B/135B
# [5B[5A[2K
# 87dffdaee0b6: Extracting     135B/135B
# [5B2025-03-15 05:59:00.562Z: [5A[2K
# 87dffdaee0b6: 2025-03-15 05:59:00.563Z: Pull complete 
# [5B2025-03-15 05:59:00.567Z: [4A[2K2025-03-15 05:59:00.569Z: 
# 3f72e2f1b3f3: Extracting     223B/223B
# [4B2025-03-15 05:59:00.569Z: [4A[2K
# 3f72e2f1b3f3: Extracting     223B/223B
# [4B2025-03-15 05:59:00.589Z: [4A[2K
# 3f72e2f1b3f3: Pull complete 
# [4B2025-03-15 05:59:00.595Z: [3A[2K
# 1ac829ce5af3: Extracting     235B/235B
# [3B2025-03-15 05:59:00.596Z: [3A[2K
# 1ac829ce5af3: Extracting     235B/235B
# [3B2025-03-15 05:59:00.614Z: [3A[2K2025-03-15 05:59:00.614Z: 
# 1ac829ce5af3: Pull complete 
# [3B2025-03-15 05:59:00.632Z: [2A[2K
# 2a15ab263bdf: Extracting  557.1kB/230.6MB
# [2B2025-03-15 05:59:00.733Z: [2A[2K
# 2a15ab263bdf: Extracting  3.899MB/230.6MB
# [2B2025-03-15 05:59:00.833Z: [2A[2K
# 2a15ab263bdf: Extracting  10.03MB/230.6MB
# [2B2025-03-15 05:59:00.937Z: [2A[2K
# 2a15ab263bdf: Extracting  17.83MB/230.6MB
# [2B2025-03-15 05:59:01.055Z: [2A[2K
# 2a15ab263bdf: Extracting   23.4MB/230.6MB
# [2B2025-03-15 05:59:01.168Z: [2A[2K2025-03-15 05:59:01.168Z: 
# 2a15ab263bdf: Extracting  24.51MB/230.6MB
# [2B2025-03-15 05:59:01.281Z: [2A2025-03-15 05:59:01.282Z: [2K
# 2a15ab263bdf: Extracting  25.07MB/230.6MB
# [2B2025-03-15 05:59:01.448Z: [2A[2K
# 2a15ab263bdf: Extracting  26.18MB/230.6MB
# [2B2025-03-15 05:59:01.577Z: [2A2025-03-15 05:59:01.577Z: [2K
# 2a15ab263bdf: Extracting  29.52MB/230.6MB
# [2B2025-03-15 05:59:01.687Z: [2A[2K
# 2a15ab263bdf: 2025-03-15 05:59:01.687Z: Extracting  30.64MB/230.6MB
# [2B2025-03-15 05:59:01.786Z: [2A[2K
# 2a15ab263bdf: Extracting  36.77MB/230.6MB
# [2B2025-03-15 05:59:01.890Z: [2A2025-03-15 05:59:01.891Z: [2K
# 2a15ab263bdf: Extracting  42.34MB/230.6MB
# [2B2025-03-15 05:59:01.996Z: [2A[2K2025-03-15 05:59:01.996Z: 
# 2a15ab263bdf: Extracting  48.46MB/230.6MB
# [2B2025-03-15 05:59:02.104Z: [2A[2K
# 2a15ab263bdf: Extracting  53.48MB/230.6MB
# [2B2025-03-15 05:59:02.211Z: [2A[2K
# 2a15ab263bdf: Extracting  56.82MB/230.6MB
# [2B2025-03-15 05:59:02.323Z: [2A[2K
# 2a15ab263bdf: Extracting  60.16MB/230.6MB
# [2B2025-03-15 05:59:02.423Z: [2A2025-03-15 05:59:02.424Z: [2K
# 2a15ab263bdf: Extracting  67.96MB/230.6MB
# [2B2025-03-15 05:59:02.524Z: [2A2025-03-15 05:59:02.525Z: [2K
# 2a15ab263bdf: Extracting  81.33MB/230.6MB
# [2B2025-03-15 05:59:02.626Z: [2A2025-03-15 05:59:02.626Z: [2K
# 2a15ab263bdf: Extracting  91.91MB/230.6MB
# [2B2025-03-15 05:59:02.727Z: [2A[2K2025-03-15 05:59:02.727Z: 
# 2a15ab263bdf: Extracting  104.2MB/230.6MB
# [2B2025-03-15 05:59:02.840Z: [2A[2K
# 2a15ab263bdf: Extracting  113.6MB/230.6MB
# [2B2025-03-15 05:59:02.954Z: [2A[2K
# 2a15ab263bdf: Extracting  116.4MB/230.6MB
# [2B2025-03-15 05:59:03.067Z: [2A[2K
# 2a15ab263bdf: Extracting  119.2MB/230.6MB
# [2B2025-03-15 05:59:03.176Z: [2A[2K
# 2a15ab263bdf: Extracting  120.9MB/230.6MB
# [2B2025-03-15 05:59:03.284Z: [2A[2K
# 2a15ab263bdf: Extracting    122MB/230.6MB
# [2B2025-03-15 05:59:03.389Z: [2A[2K2025-03-15 05:59:03.390Z: 
# 2a15ab263bdf: Extracting  128.7MB/230.6MB
# [2B2025-03-15 05:59:03.496Z: [2A[2K
# 2a15ab263bdf: Extracting  134.3MB/230.6MB
# [2B2025-03-15 05:59:03.601Z: [2A[2K2025-03-15 05:59:03.602Z: 
# 2025-03-15 05:59:03.602Z: 2a15ab263bdf: Extracting  142.6MB/230.6MB
# [2B2025-03-15 05:59:03.702Z: [2A[2K
# 2a15ab263bdf: Extracting  148.7MB/230.6MB
# [2B2025-03-15 05:59:03.806Z: [2A[2K
# 2025-03-15 05:59:03.806Z: 2a15ab263bdf: Extracting  157.1MB/230.6MB
# [2B2025-03-15 05:59:03.908Z: [2A[2K
# 2a15ab263bdf: Extracting  163.8MB/230.6MB
# [2B2025-03-15 05:59:04.008Z: [2A[2K
# 2a15ab263bdf: Extracting  170.5MB/230.6MB
# 2025-03-15 05:59:04.008Z: [2B2025-03-15 05:59:04.116Z: [2A2025-03-15 05:59:04.118Z: [2K
# 2a15ab263bdf: Extracting  178.8MB/230.6MB
# [2B2025-03-15 05:59:04.220Z: [2A[2K
# 2a15ab263bdf: 2025-03-15 05:59:04.220Z: Extracting  186.6MB/230.6MB
# [2B2025-03-15 05:59:04.322Z: [2A2025-03-15 05:59:04.322Z: [2K
# 2a15ab263bdf: Extracting  194.4MB/230.6MB
# [2B2025-03-15 05:59:04.426Z: [2A[2K
# 2a15ab263bdf: 2025-03-15 05:59:04.426Z: Extracting  202.8MB/230.6MB
# [2B2025-03-15 05:59:04.542Z: [2A[2K
# 2a15ab263bdf: Extracting  210.6MB/230.6MB
# [2B2025-03-15 05:59:04.643Z: [2A[2K
# 2a15ab263bdf: 2025-03-15 05:59:04.644Z: Extracting  218.4MB/230.6MB
# [2B2025-03-15 05:59:04.764Z: [2A[2K
# 2a15ab263bdf: Extracting  221.7MB/230.6MB
# [2B2025-03-15 05:59:04.891Z: [2A[2K2025-03-15 05:59:04.892Z: 
# 2a15ab263bdf: Extracting  222.8MB/230.6MB
# [2B2025-03-15 05:59:05.025Z: [2A[2K
# 2a15ab263bdf: 2025-03-15 05:59:05.026Z: Extracting  224.5MB/230.6MB
# [2B2025-03-15 05:59:05.218Z: [2A[2K
# 2a15ab263bdf: Extracting  226.2MB/230.6MB
# [2B2025-03-15 05:59:05.536Z: [2A2025-03-15 05:59:05.536Z: [2K
# 2025-03-15 05:59:05.537Z: 2a15ab263bdf: Extracting  227.8MB/230.6MB
# [2B2025-03-15 05:59:05.751Z: [2A[2K2025-03-15 05:59:05.751Z: 
# 2a15ab263bdf: Extracting  228.4MB/230.6MB
# [2B2025-03-15 05:59:05.770Z: [2A[2K
# 2a15ab263bdf: 2025-03-15 05:59:05.770Z: Extracting  230.6MB/230.6MB
# [2B2025-03-15 05:59:12.461Z: [2A[2K
# 2a15ab263bdf: Pull complete 
# [2B2025-03-15 05:59:12.483Z: [1A[2K
# a9bdcaa5c876: Extracting  458.8kB/43.41MB
# [1B2025-03-15 05:59:12.605Z: [1A[2K2025-03-15 05:59:12.605Z: 
# a9bdcaa5c876: Extracting  4.588MB/43.41MB
# [1B2025-03-15 05:59:12.730Z: [1A[2K
# a9bdcaa5c876: Extracting  5.046MB/43.41MB
# [1B2025-03-15 05:59:12.865Z: [1A[2K
# a9bdcaa5c876: Extracting  7.799MB/43.41MB
# [1B2025-03-15 05:59:13.041Z: [1A2025-03-15 05:59:13.042Z: [2K
# a9bdcaa5c876: Extracting  12.39MB/43.41MB
# [1B2025-03-15 05:59:13.167Z: [1A[2K2025-03-15 05:59:13.168Z: 
# a9bdcaa5c876: Extracting  12.85MB/43.41MB
# [1B2025-03-15 05:59:13.270Z: [1A2025-03-15 05:59:13.271Z: [2K
# a9bdcaa5c876: Extracting  17.43MB/43.41MB
# [1B2025-03-15 05:59:13.372Z: [1A[2K
# a9bdcaa5c876: Extracting  22.02MB/43.41MB
# [1B2025-03-15 05:59:13.479Z: [1A2025-03-15 05:59:13.479Z: [2K
# a9bdcaa5c876: Extracting  27.98MB/43.41MB
# [1B2025-03-15 05:59:13.705Z: [1A2025-03-15 05:59:13.705Z: [2K
# a9bdcaa5c876: Extracting  29.82MB/43.41MB
# [1B2025-03-15 05:59:13.847Z: [1A[2K
# a9bdcaa5c876: Extracting  30.74MB/43.41MB
# [1B2025-03-15 05:59:13.953Z: [1A[2K
# a9bdcaa5c876: Extracting   31.2MB/43.41MB
# [1B2025-03-15 05:59:14.066Z: [1A[2K
# a9bdcaa5c876: Extracting  31.65MB/43.41MB
# [1B2025-03-15 05:59:14.210Z: [1A[2K
# a9bdcaa5c876: Extracting  33.03MB/43.41MB
# [1B2025-03-15 05:59:14.405Z: [1A2025-03-15 05:59:14.406Z: [2K
# a9bdcaa5c876: Extracting  36.24MB/43.41MB
# [1B2025-03-15 05:59:14.534Z: [1A[2K
# a9bdcaa5c876: Extracting  38.99MB/43.41MB
# [1B2025-03-15 05:59:14.688Z: [1A[2K2025-03-15 05:59:14.689Z: 
# a9bdcaa5c876: Extracting  40.37MB/43.41MB
# [1B2025-03-15 05:59:14.887Z: [1A[2K
# a9bdcaa5c876: Extracting  41.29MB/43.41MB
# [1B2025-03-15 05:59:14.906Z: [1A[2K2025-03-15 05:59:14.907Z: 
# a9bdcaa5c876: Extracting  43.41MB/43.41MB
# [1B2025-03-15 05:59:16.267Z: [1A[2K
# a9bdcaa5c876: Pull complete 
# [1B2025-03-15 05:59:16.276Z: Digest: sha256:5212d8ed44c89bfadad14a03104ef75b09c5de8642a58721c271f2e9155f5023
# 2025-03-15 05:59:16.279Z: Status: Downloaded newer image for mcr.microsoft.com/devcontainers/base:alpine
# 2025-03-15 05:59:16.421Z: Container started
# 2025-03-15 05:59:16.630Z: Outcome: success User: vscode WorkspaceFolder: /workspaces/PythonThinker2-CT07-StudentsCopy-v2
# 2025-03-15 05:59:16.638Z: devcontainer process exited with exit code 0

# =================================================================================
# 2025-03-15 05:59:17.036Z: Running blocking commands...
# 2025-03-15 05:59:17.082Z: $ devcontainer up --id-label Type=codespaces --workspace-folder /var/lib/docker/codespacemount/workspace/PythonThinker2-CT07-StudentsCopy-v2 --mount type=bind,source=/.codespaces/agent/mount/cache,target=/vscode --user-data-folder /var/lib/docker/codespacemount/.persistedshare --container-data-folder .vscode-remote/data/Machine --container-system-data-folder /var/vscode-remote --log-level trace --log-format json --update-remote-user-uid-default never --mount-workspace-git-root false --omit-config-remote-env-from-metadata --skip-non-blocking-commands --expect-existing-container --config "/var/lib/docker/codespacemount/workspace/PythonThinker2-CT07-StudentsCopy-v2/.devcontainer/devcontainer.json" --override-config /root/.codespaces/shared/merged_devcontainer.json --default-user-env-probe loginInteractiveShell --container-session-data-folder /workspaces/.codespaces/.persistedshare/devcontainers-cli/cache --secrets-file /root/.codespaces/shared/user-secrets-envs.json
# 2025-03-15 05:59:17.398Z: @devcontainers/cli 0.68.0. Node.js v18.20.6. linux 6.8.0-1021-azure x64.
# 2025-03-15 05:59:17.776Z: Outcome: success User: vscode WorkspaceFolder: /workspaces/PythonThinker2-CT07-StudentsCopy-v2
# 2025-03-15 05:59:17.797Z: devcontainer process exited with exit code 0

# =================================================================================
# 2025-03-15 05:59:17.841Z: Configuring codespace...

# =================================================================================
# 2025-03-15 05:59:17.843Z: Finished configuring codespace.
