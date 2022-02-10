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
              "data": "\"\"\"\n========================\n3D plot projection types\n========================\n\nDemonstrates the different camera projections for 3D plots, and the effects of\nchanging the focal length for a perspective projection. Note that Matplotlib\ncorrects for the 'zoom' effect of changing the focal length.\n\nThe default focal length of 1 corresponds to a Field of View (FOV) of 90 deg.\nAn increased focal length between 1 and infinity \"flattens\" the image, while a\ndecreased focal length between 1 and 0 exaggerates the perspective and gives\nthe image more apparent depth. In the limiting case, a focal length of\ninfinity corresponds to an orthographic projection after correction of the\nzoom effect.\n\nYou can calculate focal length from a FOV via the equation:\n\n.. mathmpl::\n\n    1 / \\tan (FOV / 2)\n\nOr vice versa:\n\n.. mathmpl::\n\n    FOV = 2 * \\atan (1 / focal length)\n\n\"\"\""
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
              "data": "from"
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
              "data": "mpl_toolkits"
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
              "data": "mplot3d"
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
            "type": "",
            "link": {
              "type": "str",
              "data": "axes3d"
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
                  "version": "3.5.1",
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
              "data": "1"
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
              "data": "3"
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
              "data": "subplot_kw"
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
              "data": "projection"
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
              "data": "3d"
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
              "data": "\n"
            }
          },
          {
            "type": "c1",
            "link": {
              "type": "str",
              "data": "# Get the test data"
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
              "data": "X"
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
              "data": "Y"
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
              "data": "Z"
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
              "data": "axes3d"
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
              "data": "get_test_data"
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
              "data": "0.05"
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
              "data": "# Plot the data"
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
              "data": "plot_wireframe"
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
              "data": "X"
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
              "data": "Y"
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
              "data": "Z"
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
              "data": "rstride"
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
            "type": "",
            "link": {
              "type": "str",
              "data": "cstride"
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
              "data": "# Set the orthographic projection."
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
              "data": "set_proj_type"
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
              "data": "ortho"
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
              "data": "  "
            }
          },
          {
            "type": "c1",
            "link": {
              "type": "str",
              "data": "# FOV = 0 deg"
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
              "data": "set_title"
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
            "type": "s2",
            "link": {
              "type": "str",
              "data": "\""
            }
          },
          {
            "type": "s2",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s2",
            "link": {
              "type": "str",
              "data": "ortho"
            }
          },
          {
            "type": "s2",
            "link": {
              "type": "str",
              "data": "'"
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
            "type": "s2",
            "link": {
              "type": "str",
              "data": "focal_length = \u221e"
            }
          },
          {
            "type": "s2",
            "link": {
              "type": "str",
              "data": "\""
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
              "data": "# Set the perspective projections"
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
              "data": "set_proj_type"
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
              "data": "persp"
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
              "data": "  "
            }
          },
          {
            "type": "c1",
            "link": {
              "type": "str",
              "data": "# FOV = 90 deg"
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
              "data": "set_title"
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
            "type": "s2",
            "link": {
              "type": "str",
              "data": "\""
            }
          },
          {
            "type": "s2",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s2",
            "link": {
              "type": "str",
              "data": "persp"
            }
          },
          {
            "type": "s2",
            "link": {
              "type": "str",
              "data": "'"
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
            "type": "s2",
            "link": {
              "type": "str",
              "data": "focal_length = 1 (default)"
            }
          },
          {
            "type": "s2",
            "link": {
              "type": "str",
              "data": "\""
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
              "data": "2"
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
              "data": "set_proj_type"
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
              "data": "persp"
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
              "data": "focal_length"
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
              "data": "0.2"
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
              "data": "# FOV = 157.4 deg"
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
              "data": "2"
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
              "data": "set_title"
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
            "type": "s2",
            "link": {
              "type": "str",
              "data": "\""
            }
          },
          {
            "type": "s2",
            "link": {
              "type": "str",
              "data": "'"
            }
          },
          {
            "type": "s2",
            "link": {
              "type": "str",
              "data": "persp"
            }
          },
          {
            "type": "s2",
            "link": {
              "type": "str",
              "data": "'"
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
            "type": "s2",
            "link": {
              "type": "str",
              "data": "focal_length = 0.2"
            }
          },
          {
            "type": "s2",
            "link": {
              "type": "str",
              "data": "\""
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
        "ce_status": "None"
      }
    }
  ],
  "title": null
}