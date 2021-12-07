{
  "children": [
    {
      "type": "Code2",
      "data": {
        "entries": [
          {
            "type": "sd",
            "link": {
              "type": "str",
              "data": "\"\"\"\n==================\nAnscombe's quartet\n==================\n\n`Anscombe's quartet`_ is a group of datasets (x, y) that have the same mean,\nstandard deviation, and regression line, but which are qualitatively different.\n\nIt is often used to illustrate the importance of looking at a set of data\ngraphically and not only relying on basic statistic properties.\n\n.. _Anscombe's quartet: https://en.wikipedia.org/wiki/Anscombe%27s_quartet\n\"\"\""
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "kn",
            "link": {
              "type": "str",
              "data": "import"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "nn",
            "link": {
              "type": "Link",
              "data": {
                "value": "matplotlib",
                "reference": {
                  "module": "matplotlib",
                  "version": "3.5.0",
                  "kind": "module",
                  "path": "matplotlib"
                },
                "kind": "module",
                "exists": true
              }
            }
          },
          {
            "type": "nn",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "nn",
            "link": {
              "type": "str",
              "data": "pyplot"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "as"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "nn",
            "link": {
              "type": "str",
              "data": "plt"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "kn",
            "link": {
              "type": "str",
              "data": "import"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "nn",
            "link": {
              "type": "Link",
              "data": {
                "value": "numpy",
                "reference": {
                  "module": "numpy",
                  "version": "1.21.3",
                  "kind": "module",
                  "path": "numpy"
                },
                "kind": "module",
                "exists": true
              }
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "as"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "nn",
            "link": {
              "type": "str",
              "data": "np"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "x"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "["
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "10"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "8"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "13"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "9"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "11"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "14"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "6"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "4"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "12"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "7"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "5"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "]"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "y1"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "["
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "8.04"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "6.95"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "7.58"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "8.81"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "8.33"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "9.96"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "7.24"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "4.26"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "10.84"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "4.82"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "5.68"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "]"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "y2"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "["
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "9.14"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "8.14"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "8.74"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "8.77"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "9.26"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "8.10"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "6.13"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "3.10"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "9.13"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "7.26"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "4.74"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "]"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "y3"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "["
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "7.46"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "6.77"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "12.74"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "7.11"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "7.81"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "8.84"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "6.08"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "5.39"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "8.15"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "6.42"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "5.73"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "]"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "x4"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "["
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "8"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "8"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "8"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "8"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "8"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "8"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "8"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "19"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "8"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "8"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "8"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "]"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "y4"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "["
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "6.58"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "5.76"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "7.71"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "8.84"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "8.47"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "7.04"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "5.25"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "12.50"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "5.56"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "7.91"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "6.89"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "]"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "datasets"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "{"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "I"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "x"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "y1"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "II"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "x"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "y2"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "III"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "x"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "y3"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "IV"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "x4"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "y4"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "}"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "fig"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "axs"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "plt"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "subplots"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "2"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "2"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "sharex"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "kc",
            "link": {
              "type": "str",
              "data": "True"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "sharey"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "kc",
            "link": {
              "type": "str",
              "data": "True"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "figsize"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "6"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "6"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "                        "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "gridspec_kw"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "{"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "wspace"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "0.08"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "hspace"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "0.08"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "}"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "axs"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "["
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "0"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "0"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "]"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "set"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "xlim"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "0"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "20"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ylim"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "2"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "14"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "axs"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "["
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "0"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "0"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "]"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "set"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "xticks"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "0"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "10"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "20"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "yticks"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "4"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "8"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "12"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "k",
            "link": {
              "type": "str",
              "data": "for"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ax"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "label"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "x"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "y"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "ow",
            "link": {
              "type": "str",
              "data": "in"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "nb",
            "link": {
              "type": "str",
              "data": "zip"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "axs"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "flat"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "datasets"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "items"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ax"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "text"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "0.1"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "0.9"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "label"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "fontsize"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "20"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "transform"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ax"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "transAxes"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "va"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "top"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ax"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "tick_params"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "direction"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "in"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "top"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "kc",
            "link": {
              "type": "str",
              "data": "True"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "right"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "kc",
            "link": {
              "type": "str",
              "data": "True"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ax"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "plot"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "x"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "y"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "o"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "c1",
            "link": {
              "type": "str",
              "data": "# linear regression"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "p1"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "p0"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "np"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "polyfit"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "x"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "y"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "deg"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "1"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "  "
            }
          },
          {
            "type": "c1",
            "link": {
              "type": "str",
              "data": "# slope, intercept"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ax"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "axline"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "xy1"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "0"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "p0"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "slope"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "p1"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "color"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "r"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "lw"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "2"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "c1",
            "link": {
              "type": "str",
              "data": "# add text box for the statistics"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "stats"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "sa",
            "link": {
              "type": "str",
              "data": "f"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "$"
            }
          },
          {
            "type": "se",
            "link": {
              "type": "str",
              "data": "\\\\"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "mu$ = "
            }
          },
          {
            "type": "si",
            "link": {
              "type": "str",
              "data": "{"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "np"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "mean"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "y"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "si",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": ".2f"
            }
          },
          {
            "type": "si",
            "link": {
              "type": "str",
              "data": "}"
            }
          },
          {
            "type": "se",
            "link": {
              "type": "str",
              "data": "\\n"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "             "
            }
          },
          {
            "type": "sa",
            "link": {
              "type": "str",
              "data": "f"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "$"
            }
          },
          {
            "type": "se",
            "link": {
              "type": "str",
              "data": "\\\\"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "sigma$ = "
            }
          },
          {
            "type": "si",
            "link": {
              "type": "str",
              "data": "{"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "np"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "std"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "y"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "si",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": ".2f"
            }
          },
          {
            "type": "si",
            "link": {
              "type": "str",
              "data": "}"
            }
          },
          {
            "type": "se",
            "link": {
              "type": "str",
              "data": "\\n"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "             "
            }
          },
          {
            "type": "sa",
            "link": {
              "type": "str",
              "data": "f"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "$r$ = "
            }
          },
          {
            "type": "si",
            "link": {
              "type": "str",
              "data": "{"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "np"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "corrcoef"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "x"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "y"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "["
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "0"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "]"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "["
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "1"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "]"
            }
          },
          {
            "type": "si",
            "link": {
              "type": "str",
              "data": ":"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": ".2f"
            }
          },
          {
            "type": "si",
            "link": {
              "type": "str",
              "data": "}"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "bbox"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "nb",
            "link": {
              "type": "str",
              "data": "dict"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "boxstyle"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "round"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "fc"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "blanchedalmond"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ec"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "orange"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "alpha"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "0.5"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "    "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ax"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "text"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "0.95"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "mf",
            "link": {
              "type": "str",
              "data": "0.07"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "stats"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "fontsize"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "mi",
            "link": {
              "type": "str",
              "data": "9"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "bbox"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "bbox"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "            "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "transform"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "ax"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "transAxes"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ","
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": " "
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "horizontalalignment"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "="
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "right"
            }
          },
          {
            "type": "s1",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "plt"
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "."
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "show"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "("
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": ")"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "c1",
            "link": {
              "type": "str",
              "data": "#############################################################################"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "c1",
            "link": {
              "type": "str",
              "data": "#"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "c1",
            "link": {
              "type": "str",
              "data": "# .. admonition:: References"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "c1",
            "link": {
              "type": "str",
              "data": "#"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "c1",
            "link": {
              "type": "str",
              "data": "#    The use of the following functions, methods, classes and modules is shown"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "c1",
            "link": {
              "type": "str",
              "data": "#    in this example:"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "c1",
            "link": {
              "type": "str",
              "data": "#"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "c1",
            "link": {
              "type": "str",
              "data": "#    - `matplotlib.axes.Axes.axline` / `matplotlib.pyplot.axline`"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "c1",
            "link": {
              "type": "str",
              "data": "#    - `matplotlib.axes.Axes.text` / `matplotlib.pyplot.text`"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          },
          {
            "type": "c1",
            "link": {
              "type": "str",
              "data": "#    - `matplotlib.axes.Axes.tick_params` / matplotlib.pyplot.tick_params`"
            }
          },
          {
            "type": "",
            "link": {
              "type": "str",
              "data": "\n"
            }
          }
        ],
        "out": "",
        "ce_status": "execed"
      }
    },
    {
      "type": "Fig",
      "data": {
        "value": "ex-anscombe.py-0.png"
      }
    }
  ],
  "title": null
}