{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "DXPMB4syxTCF",
        "outputId": "6c368e11-3749-4704-8f0d-bcf0a0042aa9",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Password to access Ngrok is >>> dolnuigm <<<\n",
            "Code Server can be accessed on: NgrokTunnel: \"https://d347-35-226-41-130.ngrok.io\" -> \"http://localhost:10000\"\n",
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n",
            "[2022-07-15T01:54:12.811Z] info  code-server 3.10.2 387b12ef4ca404ffd39d84834e1f0776e9e3c005\n",
            "[2022-07-15T01:54:12.813Z] info  Using user-data-dir ~/.local/share/code-server\n",
            "[2022-07-15T01:54:12.832Z] info  Using config file ~/.config/code-server/config.yaml\n",
            "[2022-07-15T01:54:12.832Z] info  HTTP server listening on http://127.0.0.1:10000 \n",
            "[2022-07-15T01:54:12.832Z] info    - Authentication is enabled\n",
            "[2022-07-15T01:54:12.832Z] info      - Using password from $PASSWORD\n",
            "[2022-07-15T01:54:12.832Z] info    - Not serving HTTPS \n"
          ]
        }
      ],
      "source": [
        "#@title Colab-VSCode\n",
        "#@markdown Run this cell to access VS Code on your browser powered by Google Colab.\n",
        "\n",
        "#@markdown *This service uses [ngrok](https://ngrok.com/) to generate a URL for VS Code. To proceed, enter your [ngrok auth token](https://dashboard.ngrok.com/get-started/your-authtoken) below or [sign up](https://dashboard.ngrok.com/signup) for a ngrok account.*\n",
        "\n",
        "# Install colabcode and ngrok\n",
        "!pip install --quiet colabcode pyngrok &> /dev/null\n",
        "\n",
        "import random\n",
        "import string\n",
        "\n",
        "from colabcode import ColabCode\n",
        "from pyngrok import ngrok\n",
        "\n",
        "ngrok_authtoken = \"2BvR5rTCGCW2tnTXbg7sZNCnPvh_7yN95AH9SycTBLTbWNLfH\" #@param {type: \"string\"}\n",
        "\n",
        "#@markdown Enabling password for Ngrok is highly recommended. Otherwise, anyone with the ngrok URL will be able to access the environment.\n",
        "enable_password = True #@param {type:\"boolean\"}\n",
        "#@markdown Mount Google Drive to the path `/content/drive`\n",
        "mount_gdrive = True #@param {type:\"boolean\"}\n",
        "\n",
        "password = ''.join(random.choice(string.ascii_lowercase) for i in range(8))\n",
        "\n",
        "if enable_password and mount_gdrive:\n",
        "  ngrok.set_auth_token(ngrok_authtoken)\n",
        "  print(\"Password to access Ngrok is >>>\", password, \"<<<\")\n",
        "  ColabCode(port=10000, password=password, mount_drive=True)\n",
        "elif enable_password and not mount_gdrive:\n",
        "  ngrok.set_auth_token(ngrok_authtoken)\n",
        "  print(\"Password to access Ngrok is >>>\", password, \"<<<\")\n",
        "  ColabCode(port=10000, password=password)\n",
        "elif not enable_password and mount_gdrive:\n",
        "  ColabCode(port=10000, mount_drive=True)\n",
        "else:\n",
        "  ColabCode(port=10000)\n",
        "\n",
        "#@markdown *If you want to access the underlying GPU, change your runtime type to GPU before running. Check [colab-vscode documentation](https://github.com/derekchia/colab-vscode) for more details.*"
      ]
    }
  ],
  "metadata": {
    "accelerator": "GPU",
    "colab": {
      "collapsed_sections": [],
      "name": "ngrok(エングロック)",
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}