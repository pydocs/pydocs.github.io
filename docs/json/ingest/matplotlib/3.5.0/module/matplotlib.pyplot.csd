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
                  "value": "The cross spectral density "
                }
              },
              {
                "type": "Math",
                "data": {
                  "value": [
                    "P_{xy}"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " by Welch's average periodogram method.  The vectors "
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
                  "value": " are divided into "
                }
              },
              {
                "type": "Emph",
                "data": {
                  "value": {
                    "value": "NFFT"
                  }
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " length segments.  Each segment is detrended by function "
                }
              },
              {
                "type": "Emph",
                "data": {
                  "value": {
                    "value": "detrend"
                  }
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " and windowed by function "
                }
              },
              {
                "type": "Emph",
                "data": {
                  "value": {
                    "value": "window"
                  }
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ".  "
                }
              },
              {
                "type": "Emph",
                "data": {
                  "value": {
                    "value": "noverlap"
                  }
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " gives the length of the overlap between segments.  The product of the direct FFTs of "
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
                  "value": " are averaged over each segment to compute "
                }
              },
              {
                "type": "Math",
                "data": {
                  "value": [
                    "P_{xy}"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ", with a scaling to correct for power loss due to windowing."
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
                  "value": "If len("
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
                  "value": ") < "
                }
              },
              {
                "type": "Emph",
                "data": {
                  "value": {
                    "value": "NFFT"
                  }
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " or len("
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
                  "value": ") < "
                }
              },
              {
                "type": "Emph",
                "data": {
                  "value": {
                    "value": "NFFT"
                  }
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": ", they will be zero padded to "
                }
              },
              {
                "type": "Emph",
                "data": {
                  "value": {
                    "value": "NFFT"
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
                "type": "Words",
                "data": {
                  "value": "For plotting, the power is plotted as "
                }
              },
              {
                "type": "Math",
                "data": {
                  "value": [
                    "10 \\log_{10}(P_{xy})"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " for decibels, though "
                }
              },
              {
                "type": "Math",
                "data": {
                  "value": [
                    "P_{xy}"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " itself is returned."
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
                        "value": "If given, the following parameters also accept a string "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "s"
                        ]
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ", which is interpreted as "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "data[s]"
                        ]
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " (unless this raises an exception):"
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
            "type_": "",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Keyword arguments control the "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": ".Line2D",
                        "reference": {
                          "module": "matplotlib",
                          "version": "3.5.0",
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
                        "value": [
                          ".Bbox"
                        ],
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
                          "version": "3.5.0",
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
                          "version": "3.5.0",
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
                          "version": "3.5.0",
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
                          "version": "3.5.0",
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
                          "version": "3.5.0",
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
                      "type": "Link",
                      "data": {
                        "value": ".AbstractPathEffect",
                        "reference": {
                          "module": "matplotlib",
                          "version": "3.5.0",
                          "kind": "module",
                          "path": "matplotlib.patheffects.AbstractPathEffect"
                        },
                        "kind": "module",
                        "exists": true
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
                          "version": "3.5.0",
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
                          "version": "3.5.0",
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
            "type_": "1-D arrays or sequences",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Arrays or sequences containing the data."
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
            "param": "Fs",
            "type_": "float, default: 2",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "The sampling frequency (samples per time unit).  It is used to calculate the Fourier frequencies, "
                      }
                    },
                    {
                      "type": "Emph",
                      "data": {
                        "value": {
                          "value": "freqs"
                        }
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ", in cycles per time unit."
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
            "type_": "callable or ndarray, default: `.window_hanning`",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "A function or a vector of length "
                      }
                    },
                    {
                      "type": "Emph",
                      "data": {
                        "value": {
                          "value": "NFFT"
                        }
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ".  To create window vectors see "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": ".window_hanning",
                        "reference": {
                          "module": "matplotlib",
                          "version": "3.5.0",
                          "kind": "module",
                          "path": "matplotlib.mlab.window_hanning"
                        },
                        "kind": "module",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ", "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": ".window_none",
                        "reference": {
                          "module": "matplotlib",
                          "version": "3.5.0",
                          "kind": "module",
                          "path": "matplotlib.mlab.window_none"
                        },
                        "kind": "module",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ", "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "numpy.blackman",
                        "reference": {
                          "module": "numpy",
                          "version": "1.21.3",
                          "kind": "module",
                          "path": "numpy.blackman"
                        },
                        "kind": "module",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ", "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "numpy.hamming",
                        "reference": {
                          "module": "numpy",
                          "version": "1.21.3",
                          "kind": "module",
                          "path": "numpy.hamming"
                        },
                        "kind": "module",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ", "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "numpy.bartlett",
                        "reference": {
                          "module": "numpy",
                          "version": "1.21.3",
                          "kind": "module",
                          "path": "numpy.bartlett"
                        },
                        "kind": "module",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ", "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "scipy.signal",
                        "reference": {
                          "module": "scipy",
                          "version": "1.7.1",
                          "kind": "module",
                          "path": "scipy.signal"
                        },
                        "kind": "module",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ", "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "scipy.signal.get_window",
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
                        "value": ", etc.  If a function is passed as the argument, it must take a data segment as an argument and return the windowed version of the segment."
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
            "param": "sides",
            "type_": "{'default', 'onesided', 'twosided'}, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Which sides of the spectrum to return. 'default' is one-sided for real data and two-sided for complex data. 'onesided' forces the return of a one-sided spectrum, while 'twosided' forces two-sided."
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
            "param": "pad_to",
            "type_": "int, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "The number of points to which the data segment is padded when performing the FFT.  This can be different from "
                      }
                    },
                    {
                      "type": "Emph",
                      "data": {
                        "value": {
                          "value": "NFFT"
                        }
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ", which specifies the number of data points used.  While not increasing the actual resolution of the spectrum (the minimum distance between resolvable peaks), this can give more points in the plot, allowing for more detail. This corresponds to the "
                      }
                    },
                    {
                      "type": "Emph",
                      "data": {
                        "value": {
                          "value": "n"
                        }
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " parameter in the call to fft(). The default is None, which sets "
                      }
                    },
                    {
                      "type": "Emph",
                      "data": {
                        "value": {
                          "value": "pad_to"
                        }
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " equal to "
                      }
                    },
                    {
                      "type": "Emph",
                      "data": {
                        "value": {
                          "value": "NFFT"
                        }
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
            "param": "NFFT",
            "type_": "int, default: 256",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "The number of data points used in each block for the FFT.  A power 2 is most efficient.  This should "
                      }
                    },
                    {
                      "type": "Emph",
                      "data": {
                        "value": {
                          "value": "NOT"
                        }
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " be used to get zero padding, or the scaling of the result will be incorrect; use "
                      }
                    },
                    {
                      "type": "Emph",
                      "data": {
                        "value": {
                          "value": "pad_to"
                        }
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " for this instead."
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
            "type_": "{'none', 'mean', 'linear'} or callable, default: 'none'",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "The function applied to each segment before fft-ing, designed to remove the mean or linear trend.  Unlike in MATLAB, where the "
                      }
                    },
                    {
                      "type": "Emph",
                      "data": {
                        "value": {
                          "value": "detrend"
                        }
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " parameter is a vector, in Matplotlib it is a function.  The "
                      }
                    },
                    {
                      "type": "Directive",
                      "data": {
                        "value": [
                          "~matplotlib.mlab"
                        ],
                        "domain": null,
                        "role": "mod"
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " module defines "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": ".detrend_none",
                        "reference": {
                          "module": "matplotlib",
                          "version": "3.5.0",
                          "kind": "module",
                          "path": "matplotlib.mlab.detrend_none"
                        },
                        "kind": "module",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ", "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": ".detrend_mean",
                        "reference": {
                          "module": "matplotlib",
                          "version": "3.5.0",
                          "kind": "module",
                          "path": "matplotlib.mlab.detrend_mean"
                        },
                        "kind": "module",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ", and "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": ".detrend_linear",
                        "reference": {
                          "module": "matplotlib",
                          "version": "3.5.0",
                          "kind": "module",
                          "path": "matplotlib.mlab.detrend_linear"
                        },
                        "kind": "module",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ", but you can use a custom function as well.  You can also use a string to choose one of the functions: 'none' calls "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": ".detrend_none",
                        "reference": {
                          "module": "matplotlib",
                          "version": "3.5.0",
                          "kind": "module",
                          "path": "matplotlib.mlab.detrend_none"
                        },
                        "kind": "module",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ". 'mean' calls "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": ".detrend_mean",
                        "reference": {
                          "module": "matplotlib",
                          "version": "3.5.0",
                          "kind": "module",
                          "path": "matplotlib.mlab.detrend_mean"
                        },
                        "kind": "module",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ". 'linear' calls "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": ".detrend_linear",
                        "reference": {
                          "module": "matplotlib",
                          "version": "3.5.0",
                          "kind": "module",
                          "path": "matplotlib.mlab.detrend_linear"
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
            "param": "scale_by_freq",
            "type_": "bool, default: True",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Whether the resulting density values should be scaled by the scaling frequency, which gives density in units of Hz^-1.  This allows for integration over the returned frequency values.  The default is True for MATLAB compatibility."
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
            "param": "noverlap",
            "type_": "int, default: 0 (no overlap)",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "The number of points of overlap between segments."
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
            "param": "Fc",
            "type_": "int, default: 0",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "The center frequency of "
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
                        "value": ", which offsets the x extents of the plot to reflect the frequency range used when a signal is acquired and then filtered and downsampled to baseband."
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
            "param": "return_line",
            "type_": "bool, default: False",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Whether to include the line object plotted in the returned values."
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
            "param": "Pxy",
            "type_": "1-D array",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "The values for the cross spectrum "
                      }
                    },
                    {
                      "type": "Math",
                      "data": {
                        "value": [
                          "P_{xy}"
                        ]
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " before scaling (complex valued)."
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
            "param": "freqs",
            "type_": "1-D array",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "The frequencies corresponding to the elements in "
                      }
                    },
                    {
                      "type": "Emph",
                      "data": {
                        "value": {
                          "value": "Pxy"
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
              }
            ]
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "line",
            "type_": "`~matplotlib.lines.Line2D`",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "The line created by this function. Only returned if "
                      }
                    },
                    {
                      "type": "Emph",
                      "data": {
                        "value": {
                          "value": "return_line"
                        }
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " is True."
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
                  "value": "Plot the cross-spectral density."
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
      "module": "matplotlib",
      "version": "3.5.0",
      "kind": "module",
      "path": "matplotlib.mlab.window_hanning"
    },
    {
      "module": "matplotlib",
      "version": "3.5.0",
      "kind": "module",
      "path": "matplotlib._enums.CapStyle"
    },
    {
      "module": "matplotlib",
      "version": "3.5.0",
      "kind": "module",
      "path": "matplotlib.mlab.detrend_linear"
    },
    {
      "module": "matplotlib",
      "version": "3.5.0",
      "kind": "module",
      "path": "matplotlib.mlab.detrend_none"
    },
    {
      "module": "scipy",
      "version": "1.7.1",
      "kind": "module",
      "path": "scipy.signal.windows.windows.get_window"
    },
    {
      "module": "numpy",
      "version": "1.21.3",
      "kind": "module",
      "path": "numpy.bartlett"
    },
    {
      "module": "matplotlib",
      "version": "3.5.0",
      "kind": "module",
      "path": "matplotlib.patheffects.AbstractPathEffect"
    },
    {
      "module": "matplotlib",
      "version": "3.5.0",
      "kind": "module",
      "path": "matplotlib.lines.Line2D"
    },
    {
      "module": "numpy",
      "version": "1.21.3",
      "kind": "module",
      "path": "numpy.hamming"
    },
    {
      "module": "matplotlib",
      "version": "3.5.0",
      "kind": "module",
      "path": "matplotlib.markers.MarkerStyle"
    },
    {
      "module": "scipy",
      "version": "1.7.1",
      "kind": "module",
      "path": "scipy.signal"
    },
    {
      "module": "matplotlib",
      "version": "3.5.0",
      "kind": "module",
      "path": "matplotlib.figure.Figure"
    },
    {
      "module": "matplotlib",
      "version": "3.5.0",
      "kind": "module",
      "path": "matplotlib.mlab.detrend_mean"
    },
    {
      "module": "numpy",
      "version": "1.21.3",
      "kind": "module",
      "path": "numpy.blackman"
    },
    {
      "module": "matplotlib",
      "version": "3.5.0",
      "kind": "module",
      "path": "matplotlib.mlab.window_none"
    },
    {
      "module": "matplotlib",
      "version": "3.5.0",
      "kind": "module",
      "path": "matplotlib._enums.JoinStyle"
    },
    {
      "module": "matplotlib",
      "version": "3.5.0",
      "kind": "module",
      "path": "matplotlib.path.Path"
    }
  ],
  "ordered_sections": [
    "Summary",
    "Extended Summary",
    "Parameters",
    "Returns",
    "Other Parameters",
    "See Also",
    "Notes",
    "References"
  ],
  "item_file": "/matplotlib/pyplot.py",
  "item_line": 2490,
  "item_type": "<class 'function'>",
  "aliases": [
    "matplotlib.pyplot.csd"
  ],
  "example_section_data": {
    "children": [],
    "title": null
  },
  "see_also": [
    {
      "name": {
        "name": "psd",
        "ref": "matplotlib.pyplot.psd",
        "exists": true
      },
      "descriptions": [
        {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "is equivalent to setting "
              }
            },
            {
              "type": "Verbatim",
              "data": {
                "value": [
                  "y = x"
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
      ],
      "type": null
    }
  ],
  "version": "3.5.0",
  "signature": "csd(x, y, NFFT=None, Fs=None, Fc=None, detrend=None, window=None, noverlap=None, pad_to=None, sides=None, scale_by_freq=None, return_line=None, *, data=None, **kwargs)",
  "references": null,
  "logo": "logo.png",
  "qa": "matplotlib.pyplot.csd",
  "arbitrary": []
}