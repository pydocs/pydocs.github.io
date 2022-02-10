{
  "_content": {
    "Attributes": {
      "children": [],
      "title": null
    },
    "Extended Summary": {
      "children": [
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "Call signatures::      "
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "BlockVerbatim",
          "data": {
            "value": "plot([x], y, [fmt], *, data=None, **kwargs)\nplot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)"
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "The coordinates of the points or line nodes are given by "
                }
              },
              {
                "type": "Emph",
                "data": {
                  "value": {
                    "value": "x"
                  }
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ", "
                }
              },
              {
                "type": "Emph",
                "data": {
                  "value": {
                    "value": "y"
                  }
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "."
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "The optional parameter "
                }
              },
              {
                "type": "Emph",
                "data": {
                  "value": {
                    "value": "fmt"
                  }
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " is a convenient way for defining basic formatting like color, marker and linestyle. It's a shortcut string notation described in the "
                }
              },
              {
                "type": "Emph",
                "data": {
                  "value": {
                    "value": "Notes"
                  }
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " section below."
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "BlockVerbatim",
          "data": {
            "value": ">>> plot(x, y)        # plot x and y using default line style and color\n>>> plot(x, y, 'bo')  # plot x and y using blue circle markers\n>>> plot(y)           # plot y using x as index array 0..N-1\n>>> plot(y, 'r+')     # ditto, but with red plusses"
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "You can use "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": ".Line2D",
                  "reference": {
                    "module": "matplotlib",
                    "version": "3.5.1",
                    "kind": "module",
                    "path": "matplotlib.lines.Line2D"
                  },
                  "kind": "module",
                  "exists": true
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " properties as keyword arguments for more control on the appearance. Line properties and "
                }
              },
              {
                "type": "Emph",
                "data": {
                  "value": {
                    "value": "fmt"
                  }
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " can be mixed. The following two calls yield identical results:"
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "BlockVerbatim",
          "data": {
            "value": ">>> plot(x, y, 'go--', linewidth=2, markersize=12)\n>>> plot(x, y, color='green', marker='o', linestyle='dashed',\n...      linewidth=2, markersize=12)"
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "When conflicting with "
                }
              },
              {
                "type": "Emph",
                "data": {
                  "value": {
                    "value": "fmt"
                  }
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ", keyword arguments take precedence."
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Strong",
                "data": {
                  "content": {
                    "value": "Plotting labelled data"
                  }
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "There's a convenient way for plotting objects with labelled data (i.e. data that can be accessed by index "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "obj['y']"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "). Instead of giving the data in "
                }
              },
              {
                "type": "Emph",
                "data": {
                  "value": {
                    "value": "x"
                  }
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " and "
                }
              },
              {
                "type": "Emph",
                "data": {
                  "value": {
                    "value": "y"
                  }
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ", you can provide the object in the "
                }
              },
              {
                "type": "Emph",
                "data": {
                  "value": {
                    "value": "data"
                  }
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " parameter and just give the labels for "
                }
              },
              {
                "type": "Emph",
                "data": {
                  "value": {
                    "value": "x"
                  }
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " and "
                }
              },
              {
                "type": "Emph",
                "data": {
                  "value": {
                    "value": "y"
                  }
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "  "
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "BlockVerbatim",
          "data": {
            "value": ">>> plot('xlabel', 'ylabel', data=obj)"
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "All indexable objects are supported. This could e.g. be a "
                }
              },
              {
                "type": "Directive",
                "data": {
                  "value": "dict",
                  "domain": null,
                  "role": null
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ", a "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": "pandas.DataFrame",
                  "reference": {
                    "module": "pandas",
                    "version": "1.4.0",
                    "kind": "module",
                    "path": "pandas.core.frame.DataFrame"
                  },
                  "kind": "module",
                  "exists": true
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " or a structured numpy array."
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Strong",
                "data": {
                  "content": {
                    "value": "Plotting multiple sets of data"
                  }
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "There are various ways to plot multiple sets of data."
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "BulletList",
          "data": {
            "value": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "The most straight forward way is just to call "
                      }
                    },
                    {
                      "type": "Directive",
                      "data": {
                        "value": "plot",
                        "domain": null,
                        "role": null
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " multiple times.   Example:"
                      }
                    }
                  ],
                  "inner": []
                }
              },
              {
                "type": "BlockVerbatim",
                "data": {
                  "value": ">>> plot(x1, y1, 'bo')\n>>> plot(x2, y2, 'go')"
                }
              }
            ]
          }
        },
        {
          "type": "BulletList",
          "data": {
            "value": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "If "
                      }
                    },
                    {
                      "type": "Emph",
                      "data": {
                        "value": {
                          "value": "x"
                        }
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " and/or "
                      }
                    },
                    {
                      "type": "Emph",
                      "data": {
                        "value": {
                          "value": "y"
                        }
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " are 2D arrays a separate data set will be drawn   for every column. If both "
                      }
                    },
                    {
                      "type": "Emph",
                      "data": {
                        "value": {
                          "value": "x"
                        }
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " and "
                      }
                    },
                    {
                      "type": "Emph",
                      "data": {
                        "value": {
                          "value": "y"
                        }
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " are 2D, they must have the   same shape. If only one of them is 2D with shape (N, m) the other   must have length N and will be used for every data set m."
                      }
                    }
                  ],
                  "inner": []
                }
              },
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Example:"
                      }
                    }
                  ],
                  "inner": []
                }
              },
              {
                "type": "BlockVerbatim",
                "data": {
                  "value": ">>> x = [1, 2, 3]\n>>> y = np.array([[1, 2], [3, 4], [5, 6]])\n>>> plot(x, y)"
                }
              },
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "is equivalent to:"
                      }
                    }
                  ],
                  "inner": []
                }
              },
              {
                "type": "BlockVerbatim",
                "data": {
                  "value": ">>> for col in range(y.shape[1]):\n...     plot(x, y[:, col])"
                }
              }
            ]
          }
        },
        {
          "type": "BulletList",
          "data": {
            "value": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "The third way is to specify multiple sets of "
                      }
                    },
                    {
                      "type": "Emph",
                      "data": {
                        "value": {
                          "value": "[x]"
                        }
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ", "
                      }
                    },
                    {
                      "type": "Emph",
                      "data": {
                        "value": {
                          "value": "y"
                        }
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ", "
                      }
                    },
                    {
                      "type": "Emph",
                      "data": {
                        "value": {
                          "value": "[fmt]"
                        }
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": "   groups::    "
                      }
                    }
                  ],
                  "inner": []
                }
              },
              {
                "type": "BlockVerbatim",
                "data": {
                  "value": ">>> plot(x1, y1, 'g^', x2, y2, 'g-')"
                }
              },
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "In this case, any additional keyword argument applies to all   datasets. Also this syntax cannot be combined with the "
                      }
                    },
                    {
                      "type": "Emph",
                      "data": {
                        "value": {
                          "value": "data"
                        }
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": "   parameter."
                      }
                    }
                  ],
                  "inner": []
                }
              }
            ]
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "By default, each line is assigned a different style specified by a 'style cycle'. The "
                }
              },
              {
                "type": "Emph",
                "data": {
                  "value": {
                    "value": "fmt"
                  }
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " and line property parameters are only necessary if you want explicit deviations from these defaults. Alternatively, you can also change the style cycle using "
                }
              },
              {
                "type": "Directive",
                "data": {
                  "value": "axes.prop_cycle",
                  "domain": null,
                  "role": "rc"
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "."
                }
              }
            ],
            "inner": []
          }
        }
      ],
      "title": null
    },
    "Methods": {
      "children": [],
      "title": null
    },
    "Notes": {
      "children": [
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Strong",
                "data": {
                  "content": {
                    "value": "Format Strings"
                  }
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "A format string consists of a part for color, marker and line::      "
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "BlockVerbatim",
          "data": {
            "value": "fmt = '[marker][line][color]'"
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "Each of them is optional. If not provided, the value from the style cycle is used. Exception: If "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "line"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " is given, but no "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "marker"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ", the data will be a line without markers."
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "Other combinations such as "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "[color][marker][line]"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " are also supported, but note that their parsing may be ambiguous."
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Strong",
                "data": {
                  "content": {
                    "value": "Markers"
                  }
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "=============   =============================== character       description =============   =============================== "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'.'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         point marker "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "','"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         pixel marker "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'o'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         circle marker "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'v'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         triangle_down marker "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'^'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         triangle_up marker "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'<'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         triangle_left marker "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'>'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         triangle_right marker "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'1'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         tri_down marker "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'2'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         tri_up marker "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'3'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         tri_left marker "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'4'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         tri_right marker "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'8'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         octagon marker "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'s'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         square marker "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'p'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         pentagon marker "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'P'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         plus (filled) marker "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'*'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         star marker "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'h'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         hexagon1 marker "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'H'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         hexagon2 marker "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'+'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         plus marker "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'x'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         x marker "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'X'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         x (filled) marker "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'D'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         diamond marker "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'d'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         thin_diamond marker "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'|'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         vline marker "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'_'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         hline marker =============   ==============================="
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Strong",
                "data": {
                  "content": {
                    "value": "Line Styles"
                  }
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "=============    =============================== character        description =============    =============================== "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'-'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "          solid line style "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'--'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         dashed line style "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'-.'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "         dash-dot line style "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "':'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "          dotted line style =============    ==============================="
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "Example format strings::      "
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "BlockVerbatim",
          "data": {
            "value": "'b'    # blue markers with default shape\n'or'   # red circles\n'-g'   # green solid line\n'--'   # dashed line with default color\n'^k:'  # black triangle_up markers connected by a dotted line"
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Strong",
                "data": {
                  "content": {
                    "value": "Colors"
                  }
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "The supported color abbreviations are the single letter codes"
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "=============    =============================== character        color =============    =============================== "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'b'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "          blue "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'g'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "          green "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'r'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "          red "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'c'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "          cyan "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'m'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "          magenta "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'y'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "          yellow "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'k'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "          black "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'w'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": "          white =============    ==============================="
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "and the "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'CN'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " colors that index into the default property cycle."
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "If the color is the only part of the format string, you can additionally use any  "
                }
              },
              {
                "type": "Directive",
                "data": {
                  "value": "matplotlib.colors",
                  "domain": null,
                  "role": null
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " spec, e.g. full names ("
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'green'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ") or hex strings ("
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "'#008000'"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ")."
                }
              }
            ],
            "inner": []
          }
        }
      ],
      "title": null
    },
    "Other Parameters": {
      "children": [
        {
          "type": "Param",
          "data": {
            "param": "scalex, scaley",
            "type_": "bool, default: True",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "These parameters determine if the view limits are adapted to the data limits. The values are passed on to "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "autoscale_view",
                        "reference": {
                          "module": "matplotlib",
                          "version": "3.5.1",
                          "kind": "module",
                          "path": "matplotlib.axes._base._AxesBase.autoscale_view"
                        },
                        "kind": "module",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": "."
                      }
                    }
                  ],
                  "inner": []
                }
              }
            ]
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "**kwargs",
            "type_": "`.Line2D` properties, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Emph",
                      "data": {
                        "value": {
                          "value": "kwargs"
                        }
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " are used to specify properties like a line label (for auto legends), linewidth, antialiasing, marker face color. Example::  "
                      }
                    }
                  ],
                  "inner": []
                }
              },
              {
                "type": "BlockVerbatim",
                "data": {
                  "value": ">>> plot([1, 2, 3], [1, 2, 3], 'go-', label='line 1', linewidth=2)\n>>> plot([1, 2, 3], [1, 4, 9], 'rs', label='line 2')"
                }
              },
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "If you specify multiple lines with one plot call, the kwargs apply to all those lines. In case the label object is iterable, each element is used as labels for each set of data."
                      }
                    }
                  ],
                  "inner": []
                }
              },
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Here is a list of available "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": ".Line2D",
                        "reference": {
                          "module": "matplotlib",
                          "version": "3.5.1",
                          "kind": "module",
                          "path": "matplotlib.lines.Line2D"
                        },
                        "kind": "module",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " properties:"
                      }
                    }
                  ],
                  "inner": []
                }
              },
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Properties: agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array alpha: scalar or None animated: bool antialiased or aa: bool clip_box: "
                      }
                    },
                    {
                      "type": "Directive",
                      "data": {
                        "value": ".Bbox",
                        "domain": null,
                        "role": null
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " clip_on: bool clip_path: Patch or (Path, Transform) or None color or c: color dash_capstyle: "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": ".CapStyle",
                        "reference": {
                          "module": "matplotlib",
                          "version": "3.5.1",
                          "kind": "module",
                          "path": "matplotlib._enums.CapStyle"
                        },
                        "kind": "module",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " or {'butt', 'projecting', 'round'} dash_joinstyle: "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": ".JoinStyle",
                        "reference": {
                          "module": "matplotlib",
                          "version": "3.5.1",
                          "kind": "module",
                          "path": "matplotlib._enums.JoinStyle"
                        },
                        "kind": "module",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " or {'miter', 'round', 'bevel'} dashes: sequence of floats (on/off ink in points) or (None, None) data: (2, N) array or two 1D arrays drawstyle or ds: {'default', 'steps', 'steps-pre', 'steps-mid', 'steps-post'}, default: 'default' figure: "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": ".Figure",
                        "reference": {
                          "module": "matplotlib",
                          "version": "3.5.1",
                          "kind": "module",
                          "path": "matplotlib.figure.Figure"
                        },
                        "kind": "module",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " fillstyle: {'full', 'left', 'right', 'bottom', 'top', 'none'} gid: str in_layout: bool label: object linestyle or ls: {'-', '--', '-.', ':', '', (offset, on-off-seq), ...} linewidth or lw: float marker: marker style string, "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "~.path.Path",
                        "reference": {
                          "module": "matplotlib",
                          "version": "3.5.1",
                          "kind": "module",
                          "path": "matplotlib.path.Path"
                        },
                        "kind": "module",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " or "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "~.markers.MarkerStyle",
                        "reference": {
                          "module": "matplotlib",
                          "version": "3.5.1",
                          "kind": "module",
                          "path": "matplotlib.markers.MarkerStyle"
                        },
                        "kind": "module",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " markeredgecolor or mec: color markeredgewidth or mew: float markerfacecolor or mfc: color markerfacecoloralt or mfcalt: color markersize or ms: float markevery: None or int or (int, int) or slice or list[int] or float or (float, float) or list[bool] path_effects: "
                      }
                    },
                    {
                      "type": "Directive",
                      "data": {
                        "value": ".AbstractPathEffect",
                        "domain": null,
                        "role": null
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " picker: float or callable[[Artist, Event], tuple[bool, dict]] pickradius: float rasterized: bool sketch_params: (scale: float, length: float, randomness: float) snap: bool or None solid_capstyle: "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": ".CapStyle",
                        "reference": {
                          "module": "matplotlib",
                          "version": "3.5.1",
                          "kind": "module",
                          "path": "matplotlib._enums.CapStyle"
                        },
                        "kind": "module",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " or {'butt', 'projecting', 'round'} solid_joinstyle: "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": ".JoinStyle",
                        "reference": {
                          "module": "matplotlib",
                          "version": "3.5.1",
                          "kind": "module",
                          "path": "matplotlib._enums.JoinStyle"
                        },
                        "kind": "module",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " or {'miter', 'round', 'bevel'} transform: unknown url: str visible: bool xdata: 1D array ydata: 1D array zorder: float"
                      }
                    }
                  ],
                  "inner": []
                }
              }
            ]
          }
        }
      ],
      "title": null
    },
    "Parameters": {
      "children": [
        {
          "type": "Param",
          "data": {
            "param": "x, y",
            "type_": "array-like or scalar",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "The horizontal / vertical coordinates of the data points. "
                      }
                    },
                    {
                      "type": "Emph",
                      "data": {
                        "value": {
                          "value": "x"
                        }
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " values are optional and default to "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "range(len(y))"
                        ]
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": "."
                      }
                    }
                  ],
                  "inner": []
                }
              },
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Commonly, these parameters are 1D arrays."
                      }
                    }
                  ],
                  "inner": []
                }
              },
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "They can also be scalars, or two-dimensional (in that case, the columns represent separate data sets)."
                      }
                    }
                  ],
                  "inner": []
                }
              },
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "These arguments cannot be passed as keywords."
                      }
                    }
                  ],
                  "inner": []
                }
              }
            ]
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "fmt",
            "type_": "str, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "A format string, e.g. 'ro' for red circles. See the "
                      }
                    },
                    {
                      "type": "Emph",
                      "data": {
                        "value": {
                          "value": "Notes"
                        }
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " section for a full description of the format strings."
                      }
                    }
                  ],
                  "inner": []
                }
              },
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Format strings are just an abbreviation for quickly setting basic line properties. All of these and more can also be controlled by keyword arguments."
                      }
                    }
                  ],
                  "inner": []
                }
              },
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "This argument cannot be passed as keyword."
                      }
                    }
                  ],
                  "inner": []
                }
              }
            ]
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "data",
            "type_": "indexable object, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "An object with labelled data. If given, provide the label names to plot in "
                      }
                    },
                    {
                      "type": "Emph",
                      "data": {
                        "value": {
                          "value": "x"
                        }
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " and "
                      }
                    },
                    {
                      "type": "Emph",
                      "data": {
                        "value": {
                          "value": "y"
                        }
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": "."
                      }
                    }
                  ],
                  "inner": []
                }
              },
              {
                "type": "Admonition",
                "data": {
                  "kind": "note",
                  "title": "",
                  "children": [
                    {
                      "inline": [
                        {
                          "type": "Words",
                          "data": {
                            "value": "Technically there ' s a slight ambiguity in calls where the second label is a valid *fmt*. ``plot ( ' n ' , ' o ' , data=obj)`` could be ``plt ( x, y)`` or ``plt ( y, fmt)``. In such cases, the former interpretation is chosen, but a warning is issued. You may suppress the warning by adding an empty format string ``plot ( ' n ' , ' o ' , ' ' , data=obj)``. "
                          }
                        }
                      ],
                      "inner": []
                    }
                  ]
                }
              }
            ]
          }
        }
      ],
      "title": null
    },
    "Raises": {
      "children": [],
      "title": null
    },
    "Receives": {
      "children": [],
      "title": null
    },
    "Returns": {
      "children": [
        {
          "type": "Param",
          "data": {
            "param": "",
            "type_": "list of `.Line2D`",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "A list of lines representing the plotted data."
                      }
                    }
                  ],
                  "inner": []
                }
              }
            ]
          }
        }
      ],
      "title": null
    },
    "Summary": {
      "children": [
        {
          "type": "Paragraph",
          "data": {
            "inline": [
              {
                "type": "Words",
                "data": {
                  "value": "Plot y versus x as lines and/or markers."
                }
              }
            ],
            "inner": []
          }
        }
      ],
      "title": null
    },
    "Warnings": {
      "children": [],
      "title": null
    },
    "Warns": {
      "children": [],
      "title": null
    },
    "Yields": {
      "children": [],
      "title": null
    }
  },
  "refs": [
    {
      "module": "pandas",
      "version": "1.4.0",
      "kind": "module",
      "path": "pandas.core.frame.DataFrame"
    },
    {
      "module": "matplotlib",
      "version": "3.5.1",
      "kind": "module",
      "path": "matplotlib.axes._base._AxesBase.autoscale_view"
    },
    {
      "module": "matplotlib",
      "version": "3.5.1",
      "kind": "module",
      "path": "matplotlib._enums.JoinStyle"
    },
    {
      "module": "matplotlib",
      "version": "3.5.1",
      "kind": "module",
      "path": "matplotlib.lines.Line2D"
    },
    {
      "module": "matplotlib",
      "version": "3.5.1",
      "kind": "module",
      "path": "matplotlib.markers.MarkerStyle"
    },
    {
      "module": "matplotlib",
      "version": "3.5.1",
      "kind": "module",
      "path": "matplotlib.path.Path"
    },
    {
      "module": "matplotlib",
      "version": "3.5.1",
      "kind": "module",
      "path": "matplotlib._enums.CapStyle"
    },
    {
      "module": "matplotlib",
      "version": "3.5.1",
      "kind": "module",
      "path": "matplotlib.figure.Figure"
    }
  ],
  "ordered_sections": [
    "Summary",
    "Extended Summary",
    "Parameters",
    "Returns",
    "Other Parameters",
    "See Also",
    "Notes"
  ],
  "item_file": "/matplotlib/pyplot.py",
  "item_line": 2755,
  "item_type": "<class 'function'>",
  "aliases": [
    "matplotlib.pyplot.plot"
  ],
  "example_section_data": {
    "children": [],
    "title": null
  },
  "see_also": [
    {
      "name": {
        "name": "scatter",
        "ref": "matplotlib.pyplot.scatter",
        "exists": true
      },
      "descriptions": [
        {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "XY scatter plot with markers of varying size and/or color ( sometimes also called bubble chart)."
              }
            }
          ],
          "inner": []
        }
      ],
      "type": null
    }
  ],
  "version": "3.5.1",
  "signature": "plot(*args, scalex=True, scaley=True, data=None, **kwargs)",
  "references": null,
  "logo": "logo.png",
  "qa": "matplotlib.pyplot.plot",
  "arbitrary": []
}