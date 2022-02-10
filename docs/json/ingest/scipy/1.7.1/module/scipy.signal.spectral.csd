{
  "_content": {
    "Attributes": {
      "children": [],
      "title": null
    },
    "Extended Summary": {
      "children": [],
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
                "type": "Words",
                "data": {
                  "value": "By convention, Pxy is computed with the conjugate FFT of X multiplied by the FFT of Y."
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
                  "value": "If the input series differ in length, the shorter series will be zero-padded to match."
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
                  "value": "An appropriate amount of overlap will depend on the choice of window and on your requirements. For the default Hann window an overlap of 50% is a reasonable trade off between accurately estimating the signal power, while not over counting any of the data. Narrower windows may require a larger overlap."
                }
              }
            ],
            "inner": []
          }
        },
        {
          "type": "Admonition",
          "data": {
            "kind": "versionadded",
            "title": "TODO",
            "children": [
              {
                "inline": [
                  {
                    "type": "Words",
                    "data": {
                      "value": "0.16.0 "
                    }
                  }
                ],
                "inner": []
              }
            ]
          }
        }
      ],
      "title": null
    },
    "Other Parameters": {
      "children": [],
      "title": null
    },
    "Parameters": {
      "children": [
        {
          "type": "Param",
          "data": {
            "param": "x",
            "type_": "array_like",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Time series of measurement values"
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
            "param": "y",
            "type_": "array_like",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Time series of measurement values"
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
            "param": "fs",
            "type_": "float, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Sampling frequency of the "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "x",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "x"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " and "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "y",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "y"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " time series. Defaults to 1.0."
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
            "param": "window",
            "type_": "str or tuple or array_like, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Desired window to use. If "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "window",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "window"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " is a string or tuple, it is passed to "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "get_window",
                        "reference": {
                          "module": "scipy",
                          "version": "1.7.1",
                          "kind": "module",
                          "path": "scipy.signal.windows.windows.get_window"
                        },
                        "kind": "module",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " to generate the window values, which are DFT-even by default. See "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "get_window",
                        "reference": {
                          "module": "scipy",
                          "version": "1.7.1",
                          "kind": "module",
                          "path": "scipy.signal.windows.windows.get_window"
                        },
                        "kind": "module",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " for a list of windows and required parameters. If "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "window",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "window"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " is array_like it will be used directly as the window and its length must be nperseg. Defaults to a Hann window."
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
            "param": "nperseg",
            "type_": "int, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Length of each segment. Defaults to None, but if window is str or tuple, is set to 256, and if window is array_like, is set to the length of the window."
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
            "param": "noverlap: int, optional",
            "type_": "",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Number of points to overlap between segments. If "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "None"
                        ]
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ", "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "noverlap = nperseg // 2"
                        ]
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ". Defaults to "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "None"
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
              }
            ]
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "nfft",
            "type_": "int, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Length of the FFT used, if a zero padded FFT is desired. If "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "None"
                        ]
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ", the FFT length is "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "nperseg",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "nperseg"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ". Defaults to "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "None"
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
              }
            ]
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "detrend",
            "type_": "str or function or `False`, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Specifies how to detrend each segment. If "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "detrend",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "detrend"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " is a string, it is passed as the "
                      }
                    },
                    {
                      "type": "Directive",
                      "data": {
                        "value": "type",
                        "domain": null,
                        "role": null
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " argument to the "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "detrend",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "detrend"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " function. If it is a function, it takes a segment and returns a detrended segment. If "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "detrend",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "detrend"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " is "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "False"
                        ]
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ", no detrending is done. Defaults to 'constant'."
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
            "param": "return_onesided",
            "type_": "bool, optional",
            "desc": [
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
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "True"
                        ]
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ", return a one-sided spectrum for real data. If "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "False"
                        ]
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " return a two-sided spectrum. Defaults to "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "True"
                        ]
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ", but for complex data, a two-sided spectrum is always returned."
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
            "param": "scaling",
            "type_": "{ 'density', 'spectrum' }, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Selects between computing the cross spectral density ('density') where "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "Pxy",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "Pxy"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " has units of V**2/Hz and computing the cross spectrum ('spectrum') where "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "Pxy",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "Pxy"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " has units of V**2, if "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "x",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "x"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " and "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "y",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "y"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " are measured in V and "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "fs",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "fs"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " is measured in Hz. Defaults to 'density'"
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
            "param": "axis",
            "type_": "int, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Axis along which the CSD is computed for both inputs; the default is over the last axis (i.e. "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "axis=-1"
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
            ]
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "average",
            "type_": "{ 'mean', 'median' }, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Method to use when averaging periodograms. If the spectrum is complex, the average is computed separately for the real and imaginary parts. Defaults to 'mean'."
                      }
                    }
                  ],
                  "inner": []
                }
              },
              {
                "type": "Admonition",
                "data": {
                  "kind": "versionadded",
                  "title": "TODO",
                  "children": [
                    {
                      "inline": [
                        {
                          "type": "Words",
                          "data": {
                            "value": "1.2.0 "
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
            "param": "f",
            "type_": "ndarray",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Array of sample frequencies."
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
            "param": "Pxy",
            "type_": "ndarray",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Cross spectral density or cross power spectrum of x,y."
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
                  "value": "Estimate the cross power spectral density, Pxy, using Welch's method."
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
      "module": "scipy",
      "version": "1.7.1",
      "kind": "module",
      "path": "scipy.signal.filter_design.butter"
    },
    {
      "module": "scipy",
      "version": "1.7.1",
      "kind": "module",
      "path": "scipy.signal.windows.windows.get_window"
    },
    {
      "module": "numpy",
      "version": "1.22.1",
      "kind": "module",
      "path": "numpy.random._generator.Generator"
    },
    {
      "module": "scipy",
      "version": "1.7.1",
      "kind": "module",
      "path": "scipy.signal.spectral.csd"
    },
    {
      "module": "matplotlib",
      "version": "3.5.1",
      "kind": "module",
      "path": "matplotlib.pyplot"
    },
    {
      "module": "numpy",
      "version": "1.22.1",
      "kind": "module",
      "path": "numpy.random"
    },
    {
      "module": "numpy",
      "version": "1.22.1",
      "kind": "module",
      "path": "numpy.ndarray"
    },
    {
      "module": "scipy",
      "version": "1.7.1",
      "kind": "module",
      "path": "scipy.signal"
    },
    {
      "module": "matplotlib",
      "version": "3.5.1",
      "kind": "module",
      "path": "matplotlib.pyplot.semilogy"
    },
    {
      "module": "scipy",
      "version": "1.7.1",
      "kind": "module",
      "path": "scipy._lib._util.rng_integers"
    },
    {
      "module": "numpy",
      "version": "1.22.1",
      "kind": "module",
      "path": "numpy.arange"
    },
    {
      "module": "matplotlib",
      "version": "3.5.1",
      "kind": "module",
      "path": "matplotlib.pyplot.ylabel"
    },
    {
      "module": "scipy",
      "version": "1.7.1",
      "kind": "module",
      "path": "scipy"
    },
    {
      "module": "scipy",
      "version": "1.7.1",
      "kind": "module",
      "path": "scipy.signal.signaltools.lfilter"
    },
    {
      "module": "matplotlib",
      "version": "3.5.1",
      "kind": "module",
      "path": "matplotlib.pyplot.xlabel"
    },
    {
      "module": "numpy",
      "version": "1.22.1",
      "kind": "module",
      "path": "numpy"
    },
    {
      "module": "numpy",
      "version": "1.22.1",
      "kind": "module",
      "path": "numpy.ufunc"
    },
    {
      "module": "matplotlib",
      "version": "3.5.1",
      "kind": "module",
      "path": "matplotlib.pyplot.show"
    },
    {
      "module": "numpy",
      "version": "1.22.1",
      "kind": "module",
      "path": "numpy.random._generator.default_rng"
    },
    {
      "module": "matplotlib",
      "version": "3.5.1",
      "kind": "module",
      "path": "matplotlib"
    }
  ],
  "ordered_sections": [
    "Summary",
    "Parameters",
    "Returns",
    "See Also",
    "Notes",
    "References",
    "Examples"
  ],
  "item_file": "/scipy/signal/spectral.py",
  "item_line": 456,
  "item_type": "<class 'function'>",
  "aliases": [
    "scipy.signal.csd"
  ],
  "example_section_data": {
    "children": [
      {
        "type": "Code2",
        "data": {
          "entries": [
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
                "type": "Link",
                "data": {
                  "value": "scipy",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy"
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
                "type": "Link",
                "data": {
                  "value": "signal",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy.signal"
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
                "type": "Link",
                "data": {
                  "value": "pyplot",
                  "reference": {
                    "module": "matplotlib",
                    "version": "3.5.1",
                    "kind": "module",
                    "path": "matplotlib.pyplot"
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
                "type": "Link",
                "data": {
                  "value": "plt",
                  "reference": {
                    "module": "matplotlib",
                    "version": "3.5.1",
                    "kind": "module",
                    "path": "matplotlib.pyplot"
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
                "data": "\n"
              }
            },
            {
              "type": "",
              "link": {
                "type": "Link",
                "data": {
                  "value": "rng",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy.random._generator.Generator"
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
                "type": "Link",
                "data": {
                  "value": "np",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy"
                  },
                  "kind": "module",
                  "exists": true
                }
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
                "type": "Link",
                "data": {
                  "value": "random",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy.random"
                  },
                  "kind": "module",
                  "exists": true
                }
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
                "type": "Link",
                "data": {
                  "value": "default_rng",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy.random._generator.default_rng"
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
                "data": "("
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ")"
              }
            }
          ],
          "out": "",
          "ce_status": "compiled"
        }
      },
      {
        "type": "Paragraph",
        "data": {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "Generate two test signals with some common features."
              }
            }
          ],
          "inner": []
        }
      },
      {
        "type": "Code2",
        "data": {
          "entries": [
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "fs"
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
              "type": "mf",
              "link": {
                "type": "str",
                "data": "10e3"
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
                "data": "N"
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
              "type": "mf",
              "link": {
                "type": "str",
                "data": "1e5"
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
                "data": "amp"
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
                "data": "\n"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "freq"
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
              "type": "mf",
              "link": {
                "type": "str",
                "data": "1234.0"
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
                "data": "noise_power"
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
              "type": "mf",
              "link": {
                "type": "str",
                "data": "0.001"
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
                "data": "fs"
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
                "data": "/"
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
                "data": "\n"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "time"
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
                "type": "Link",
                "data": {
                  "value": "np",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy"
                  },
                  "kind": "module",
                  "exists": true
                }
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
                "type": "Link",
                "data": {
                  "value": "arange",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy.arange"
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
                "data": "("
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "N"
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
                "data": "/"
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
                "data": "fs"
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
                "type": "Link",
                "data": {
                  "value": "b",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy.ndarray"
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
                "data": "a"
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
                "type": "Link",
                "data": {
                  "value": "signal",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy.signal"
                  },
                  "kind": "module",
                  "exists": true
                }
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
                "type": "Link",
                "data": {
                  "value": "butter",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy.signal.filter_design.butter"
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
              "type": "mf",
              "link": {
                "type": "str",
                "data": "0.25"
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
                "data": "low"
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
                "type": "Link",
                "data": {
                  "value": "rng",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy._lib._util.rng_integers"
                  },
                  "kind": "module",
                  "exists": true
                }
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
                "data": "normal"
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
                "data": "scale"
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
                "type": "Link",
                "data": {
                  "value": "np",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy"
                  },
                  "kind": "module",
                  "exists": true
                }
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
                "type": "Link",
                "data": {
                  "value": "sqrt",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy.ufunc"
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
                "data": "("
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "noise_power"
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
                "data": "size"
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
                "data": "time"
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
                "data": "shape"
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
                "data": "y"
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
                "type": "Link",
                "data": {
                  "value": "signal",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy.signal"
                  },
                  "kind": "module",
                  "exists": true
                }
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
                "type": "Link",
                "data": {
                  "value": "lfilter",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy.signal.signaltools.lfilter"
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
                "data": "("
              }
            },
            {
              "type": "",
              "link": {
                "type": "Link",
                "data": {
                  "value": "b",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy.ndarray"
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
                "data": "a"
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
                "data": "+"
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
                "data": "amp"
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
                "type": "Link",
                "data": {
                  "value": "np",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy"
                  },
                  "kind": "module",
                  "exists": true
                }
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
                "type": "Link",
                "data": {
                  "value": "sin",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy.ufunc"
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
              "type": "o",
              "link": {
                "type": "str",
                "data": "*"
              }
            },
            {
              "type": "",
              "link": {
                "type": "Link",
                "data": {
                  "value": "np",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy"
                  },
                  "kind": "module",
                  "exists": true
                }
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
                "data": "pi"
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
                "data": "freq"
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
                "data": "time"
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
                "data": "y"
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
                "type": "Link",
                "data": {
                  "value": "rng",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy._lib._util.rng_integers"
                  },
                  "kind": "module",
                  "exists": true
                }
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
                "data": "normal"
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
                "data": "scale"
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
                "data": "0.1"
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
                "type": "Link",
                "data": {
                  "value": "np",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy"
                  },
                  "kind": "module",
                  "exists": true
                }
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
                "type": "Link",
                "data": {
                  "value": "sqrt",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy.ufunc"
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
                "data": "("
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "noise_power"
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
                "data": "size"
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
                "data": "time"
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
                "data": "shape"
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ")"
              }
            }
          ],
          "out": "",
          "ce_status": "compiled"
        }
      },
      {
        "type": "Paragraph",
        "data": {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "Compute and plot the magnitude of the cross spectral density."
              }
            }
          ],
          "inner": []
        }
      },
      {
        "type": "Code2",
        "data": {
          "entries": [
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "f"
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
                "data": "Pxy"
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
                "type": "Link",
                "data": {
                  "value": "signal",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy.signal"
                  },
                  "kind": "module",
                  "exists": true
                }
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
                "type": "Link",
                "data": {
                  "value": "csd",
                  "reference": {
                    "module": "scipy",
                    "version": "1.7.1",
                    "kind": "module",
                    "path": "scipy.signal.spectral.csd"
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
                "data": "fs"
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
                "data": "nperseg"
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
                "data": "1024"
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
                "type": "Link",
                "data": {
                  "value": "plt",
                  "reference": {
                    "module": "matplotlib",
                    "version": "3.5.1",
                    "kind": "module",
                    "path": "matplotlib.pyplot"
                  },
                  "kind": "module",
                  "exists": true
                }
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
                "type": "Link",
                "data": {
                  "value": "semilogy",
                  "reference": {
                    "module": "matplotlib",
                    "version": "3.5.1",
                    "kind": "module",
                    "path": "matplotlib.pyplot.semilogy"
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
                "data": "("
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "f"
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
                "type": "Link",
                "data": {
                  "value": "np",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy"
                  },
                  "kind": "module",
                  "exists": true
                }
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
                "type": "Link",
                "data": {
                  "value": "abs",
                  "reference": {
                    "module": "numpy",
                    "version": "1.22.1",
                    "kind": "module",
                    "path": "numpy.ufunc"
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
                "data": "("
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": "Pxy"
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
                "type": "Link",
                "data": {
                  "value": "plt",
                  "reference": {
                    "module": "matplotlib",
                    "version": "3.5.1",
                    "kind": "module",
                    "path": "matplotlib.pyplot"
                  },
                  "kind": "module",
                  "exists": true
                }
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
                "type": "Link",
                "data": {
                  "value": "xlabel",
                  "reference": {
                    "module": "matplotlib",
                    "version": "3.5.1",
                    "kind": "module",
                    "path": "matplotlib.pyplot.xlabel"
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
                "data": "frequency [Hz]"
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
                "type": "Link",
                "data": {
                  "value": "plt",
                  "reference": {
                    "module": "matplotlib",
                    "version": "3.5.1",
                    "kind": "module",
                    "path": "matplotlib.pyplot"
                  },
                  "kind": "module",
                  "exists": true
                }
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
                "type": "Link",
                "data": {
                  "value": "ylabel",
                  "reference": {
                    "module": "matplotlib",
                    "version": "3.5.1",
                    "kind": "module",
                    "path": "matplotlib.pyplot.ylabel"
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
                "data": "CSD [V**2/Hz]"
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
                "type": "Link",
                "data": {
                  "value": "plt",
                  "reference": {
                    "module": "matplotlib",
                    "version": "3.5.1",
                    "kind": "module",
                    "path": "matplotlib.pyplot"
                  },
                  "kind": "module",
                  "exists": true
                }
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
                "type": "Link",
                "data": {
                  "value": "show",
                  "reference": {
                    "module": "matplotlib",
                    "version": "3.5.1",
                    "kind": "module",
                    "path": "matplotlib.pyplot.show"
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
                "data": "("
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": ")"
              }
            }
          ],
          "out": "",
          "ce_status": "compiled"
        }
      }
    ],
    "title": null
  },
  "see_also": [
    {
      "name": {
        "name": "coherence",
        "ref": "scipy.signal.spectral.coherence",
        "exists": true
      },
      "descriptions": [
        {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "Magnitude squared coherence by Welch's method."
              }
            }
          ],
          "inner": []
        }
      ],
      "type": null
    },
    {
      "name": {
        "name": "lombscargle",
        "ref": "scipy.signal.spectral.lombscargle",
        "exists": true
      },
      "descriptions": [
        {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "Lomb-Scargle periodogram for unevenly sampled data"
              }
            }
          ],
          "inner": []
        }
      ],
      "type": null
    },
    {
      "name": {
        "name": "periodogram",
        "ref": "scipy.signal.spectral.periodogram",
        "exists": true
      },
      "descriptions": [
        {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "Simple, optionally modified periodogram"
              }
            }
          ],
          "inner": []
        }
      ],
      "type": null
    },
    {
      "name": {
        "name": "welch",
        "ref": "scipy.signal.spectral.welch",
        "exists": true
      },
      "descriptions": [
        {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "Power spectral density by Welch's method. [Equivalent to csd(x,x)]"
              }
            }
          ],
          "inner": []
        }
      ],
      "type": null
    }
  ],
  "version": "1.7.1",
  "signature": "csd(x, y, fs=1.0, window='hann', nperseg=None, noverlap=None, nfft=None, detrend='constant', return_onesided=True, scaling='density', axis=-1, average='mean')",
  "references": null,
  "logo": "logo.png",
  "qa": "scipy.signal.spectral.csd",
  "arbitrary": []
}