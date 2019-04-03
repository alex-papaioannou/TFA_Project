{
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "#environment setting\n",
        "import pandas as pd\n",
        "import sqlite3\n",
        "\n",
        "# Library Import and Environment Setting needed for Logistic Regression\n",
        "\n",
        "import numpy as np\n",
        "from sklearn import preprocessing\n",
        "import matplotlib.pyplot as plt \n",
        "plt.rc(\"font\", size=14)\n",
        "from sklearn.linear_model import LogisticRegression\n",
        "from sklearn.cross_validation import train_test_split\n",
        "import seaborn as sns\n",
        "sns.set(style=\"white\")\n",
        "sns.set(style=\"whitegrid\", color_codes=True)"
      ],
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "No module named 'sklearn.cross_validation'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-1-5004c765d9a2>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     10\u001b[0m \u001b[0mplt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"font\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msize\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m14\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     11\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0msklearn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlinear_model\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mLogisticRegression\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 12\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0msklearn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcross_validation\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mtrain_test_split\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     13\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mseaborn\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0msns\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     14\u001b[0m \u001b[0msns\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mset\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mstyle\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"white\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'sklearn.cross_validation'"
          ]
        }
      ],
      "execution_count": 1,
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": [],
      "outputs": [],
      "execution_count": null,
      "metadata": {}
    }
  ],
  "metadata": {
    "kernel_info": {
      "name": "python3"
    },
    "kernelspec": {
      "name": "python3",
      "language": "python",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python",
      "version": "3.6.4",
      "mimetype": "text/x-python",
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "pygments_lexer": "ipython3",
      "nbconvert_exporter": "python",
      "file_extension": ".py"
    },
    "nteract": {
      "version": "0.12.3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 2
}