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
              "data": "\"\"\"\n==========================\nSolarized Light stylesheet\n==========================\n\nThis shows an example of \"Solarized_Light\" styling, which\ntries to replicate the styles of:\n\n- https://ethanschoonover.com/solarized/\n- https://github.com/jrnold/ggthemes\n- http://www.pygal.org/en/stable/documentation/builtin_styles.html#light-solarized\n\nand work of:\n\n- https://github.com/tonysyu/mpltools\n\nusing all 8 accents of the color palette - starting with blue\n\nStill TODO:\n\n- Create alpha values for bar and stacked charts. .33 or .5\n- Apply Layout Rules\n\"\"\""
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
              "data": "\n"
            }
          },
          {
            "type": "c1",
            "link": {
              "type": "str",
              "data": "# Fixing random state for reproducibility"
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
              "data": "random"
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
              "data": "seed"
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
              "data": "19680801"
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
              "data": "linspace"
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
            "type": "k",
            "link": {
              "type": "str",
              "data": "with"
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
              "data": "style"
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
              "data": "context"
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
              "data": "Solarize_Light2"
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
              "data": "sin"
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
            "type": "o",
            "link": {
              "type": "str",
              "data": "+"
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
              "data": "+"
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
              "data": "random"
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
              "data": "randn"
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
              "data": "50"
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
              "data": "    "
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
              "data": "sin"
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
            "type": "o",
            "link": {
              "type": "str",
              "data": "+"
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
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "*"
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
              "data": "+"
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
              "data": "random"
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
              "data": "randn"
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
              "data": "50"
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
              "data": "    "
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
              "data": "sin"
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
            "type": "o",
            "link": {
              "type": "str",
              "data": "+"
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
              "data": "3"
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
              "data": "*"
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
              "data": "+"
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
              "data": "random"
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
              "data": "randn"
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
              "data": "50"
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
              "data": "    "
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
              "data": "sin"
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
            "type": "o",
            "link": {
              "type": "str",
              "data": "+"
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
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "+"
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
              "data": "random"
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
              "data": "randn"
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
              "data": "50"
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
              "data": "    "
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
              "data": "sin"
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
            "type": "o",
            "link": {
              "type": "str",
              "data": "+"
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
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "*"
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
              "data": "+"
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
              "data": "random"
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
              "data": "randn"
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
              "data": "50"
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
              "data": "    "
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
              "data": "sin"
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
            "type": "o",
            "link": {
              "type": "str",
              "data": "+"
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
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "*"
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
              "data": "+"
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
              "data": "random"
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
              "data": "randn"
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
              "data": "50"
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
              "data": "    "
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
              "data": "sin"
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
            "type": "o",
            "link": {
              "type": "str",
              "data": "+"
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
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "*"
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
              "data": "+"
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
              "data": "random"
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
              "data": "randn"
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
              "data": "50"
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
              "data": "    "
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
              "data": "sin"
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
            "type": "o",
            "link": {
              "type": "str",
              "data": "+"
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
              "data": " "
            }
          },
          {
            "type": "o",
            "link": {
              "type": "str",
              "data": "*"
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
              "data": "+"
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
              "data": "random"
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
              "data": "randn"
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
              "data": "50"
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
              "data": "    "
            }
          },
          {
            "type": "c1",
            "link": {
              "type": "str",
              "data": "# Number of accent colors in the color scheme"
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
              "data": "title"
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
              "data": "8 Random Lines - Line"
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
              "data": "xlabel"
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
              "data": "x label"
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
              "data": "ylabel"
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
              "data": "y label"
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
          }
        ],
        "out": "",
        "ce_status": "execed"
      }
    },
    {
      "type": "Fig",
      "data": {
        "value": "ex-plot_solarizedlight2.py-0.png"
      }
    }
  ],
  "title": null
}