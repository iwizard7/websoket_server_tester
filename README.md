![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/iwizard7/websoket_server_tester) ![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/iwizard7/websoket_server_tester) [![Pylint](https://github.com/iwizard7/websoket_server_tester/actions/workflows/pylint.yml/badge.svg)](https://github.com/iwizard7/websoket_server_tester/actions/workflows/pylint.yml) [![Pylint](https://github.com/iwizard7/websoket_server_tester/actions/workflows/pylint.yml/badge.svg)](https://github.com/iwizard7/websoket_server_tester/actions/workflows/pylint.yml) [![Bandit](https://github.com/iwizard7/websoket_server_tester/actions/workflows/bandit.yml/badge.svg)](https://github.com/iwizard7/websoket_server_tester/actions/workflows/bandit.yml)
# WebSocket Server Helm Chart

🌐 Пример Helm-чарта для развертывания простого WebSocket сервера на Python.

## Описание

Этот Helm-чарт позволяет вам легко развернуть WebSocket сервер на Python с использованием Kubernetes и Helm. Он включает в себя все необходимые компоненты, такие как деплоймент, сервис и конфигурацию.

## Установка

1. Установите Helm, если у вас его еще нет:

   ```bash
   # Пример установки Helm на macOS с использованием Homebrew
   brew install helm
   ```

2. Клонируйте репозиторий на свой локальный компьютер:

   ```bash
   git clone https://github.com/iwizard7/websoket_server_tester.git
   ```

3. Перейдите в директорию проекта:

   ```bash
   cd websocket-server-chart
   ```

4. Установите чарт:

   ```bash
   helm install websocket-server .
   ```

## Конфигурация

В файле `values.yaml` вы можете настроить параметры развертывания WebSocket сервера, такие как порт, ресурсы и другие настройки.

## Использование

1. После успешной установки чарта, WebSocket сервер будет развернут в вашем кластере Kubernetes.
2. Для получения IP-адреса и порта сервера выполните команду:

   ```bash
   kubectl get service websocket-server
   ```

3. Используйте полученный IP-адрес и порт для подключения к WebSocket серверу.

## Вклад

Вы можете внести свой вклад в проект, создавая pull request'ы и открывая issues.
