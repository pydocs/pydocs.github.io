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
                  "value": "This docstring was copied from numpy.random.mtrand.RandomState.f."
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
                  "value": "Some inconsistencies with the Dask version may exist."
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
                  "value": "Samples are drawn from an F distribution with specified parameters, "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": "dfnum",
                  "reference": {
                    "module": null,
                    "version": null,
                    "kind": "local",
                    "path": "dfnum"
                  },
                  "kind": "local",
                  "exists": true
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " (degrees of freedom in numerator) and "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": "dfden",
                  "reference": {
                    "module": null,
                    "version": null,
                    "kind": "local",
                    "path": "dfden"
                  },
                  "kind": "local",
                  "exists": true
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " (degrees of freedom in denominator), where both parameters must be greater than zero."
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
                  "value": "The random variate of the F distribution (also known as the Fisher distribution) is a continuous probability distribution that arises in ANOVA tests, and is the ratio of two chi-square variates."
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
                      "value": "New code should use the ``f`` method of a ``default_rng ( )`` instance instead; please see the : ref : `random - quick - start`. "
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
                  "value": "The F statistic is used to compare in-group variances to between-group variances. Calculating the distribution depends on the sampling, and so it is a function of the respective degrees of freedom in the problem.  The variable "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": "dfnum",
                  "reference": {
                    "module": null,
                    "version": null,
                    "kind": "local",
                    "path": "dfnum"
                  },
                  "kind": "local",
                  "exists": true
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " is the number of samples minus one, the between-groups degrees of freedom, while "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": "dfden",
                  "reference": {
                    "module": null,
                    "version": null,
                    "kind": "local",
                    "path": "dfden"
                  },
                  "kind": "local",
                  "exists": true
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " is the within-groups degrees of freedom, the sum of the number of samples in each group minus the number of groups."
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
      "children": [],
      "title": null
    },
    "Parameters": {
      "children": [
        {
          "type": "Param",
          "data": {
            "param": "dfnum",
            "type_": "float or array_like of floats",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Degrees of freedom in numerator, must be > 0."
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
            "param": "dfden",
            "type_": "float or array_like of float",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Degrees of freedom in denominator, must be > 0."
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
            "param": "size",
            "type_": "int or tuple of ints, optional",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Output shape.  If the given shape is, e.g., "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "(m, n, k)"
                        ]
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": ", then "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "m * n * k"
                        ]
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " samples are drawn.  If size is "
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
                        "value": " (default), a single value is returned if "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "dfnum"
                        ]
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " and "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "dfden"
                        ]
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " are both scalars. Otherwise, "
                      }
                    },
                    {
                      "type": "Verbatim",
                      "data": {
                        "value": [
                          "np.broadcast(dfnum, dfden).size"
                        ]
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " samples are drawn."
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
            "param": "out",
            "type_": "ndarray or scalar",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Drawn samples from the parameterized Fisher distribution."
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
                  "value": "Draw samples from an F distribution."
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
      "module": "dask",
      "version": "2021.10.0",
      "kind": "module",
      "path": "dask.array.ufunc.log10"
    },
    {
      "module": "dask",
      "version": "2021.10.0",
      "kind": "module",
      "path": "dask.array.random.RandomState.f"
    },
    {
      "module": "dask",
      "version": "2021.10.0",
      "kind": "module",
      "path": "dask.array.random"
    }
  ],
  "ordered_sections": [
    "Summary",
    "Extended Summary",
    "Parameters",
    "Returns",
    "See Also",
    "Notes",
    "References",
    "Examples"
  ],
  "item_file": "/dask/array/random.py",
  "item_line": 285,
  "item_type": "<class 'function'>",
  "aliases": [
    "dask.array.random.f",
    "dask.array.linalg.RandomState.f"
  ],
  "example_section_data": {
    "children": [
      {
        "type": "Paragraph",
        "data": {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "An example from Glantz[1], pp 47-40:"
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
                "value": "Two groups, children of diabetics (25 people) and children from people without diabetes (25 controls). Fasting blood glucose was measured, case group had a mean value of 86.1, controls had a mean value of 82.2. Standard deviations were 2.09 and 2.49 respectively. Are these data consistent with the null hypothesis that the parents diabetic status does not affect their children's blood glucose levels? Calculating the F statistic from the data gives a value of 36.01."
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
                "value": "Draw samples from the distribution:"
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
                "data": "dfnum"
              }
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
                "data": "1."
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "c1",
              "link": {
                "type": "str",
                "data": "# between group degrees of freedom  # doctest: +SKIP"
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
                "data": "dfden"
              }
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
                "data": "48."
              }
            },
            {
              "type": "",
              "link": {
                "type": "str",
                "data": " "
              }
            },
            {
              "type": "c1",
              "link": {
                "type": "str",
                "data": "# within groups degrees of freedom  # doctest: +SKIP"
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
                "data": "s"
              }
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
                "type": "Link",
                "data": {
                  "value": "random",
                  "reference": {
                    "module": "dask",
                    "version": "2021.10.0",
                    "kind": "module",
                    "path": "dask.array.random"
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
                  "value": "f",
                  "reference": {
                    "module": "dask",
                    "version": "2021.10.0",
                    "kind": "module",
                    "path": "dask.array.random.RandomState.f"
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
                "data": "dfnum"
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
                "data": "dfden"
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
                "data": "1000"
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
                "data": "# doctest: +SKIP"
              }
            }
          ],
          "out": "",
          "ce_status": "execed"
        }
      },
      {
        "type": "Paragraph",
        "data": {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "The lower bound for the top 1% of the samples is :"
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
                "data": "sort"
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
                "data": "s"
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
              "type": "o",
              "link": {
                "type": "str",
                "data": "-"
              }
            },
            {
              "type": "mi",
              "link": {
                "type": "Link",
                "data": {
                  "value": "10",
                  "reference": {
                    "module": "dask",
                    "version": "2021.10.0",
                    "kind": "module",
                    "path": "dask.array.ufunc.log10"
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
                "data": "]"
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
                "data": "# doctest: +SKIP"
              }
            }
          ],
          "out": "7.61988120985 # random",
          "ce_status": "execed"
        }
      },
      {
        "type": "Paragraph",
        "data": {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "So there is about a 1% chance that the F statistic will exceed 7.62, the measured value is 36, so the null hypothesis is rejected at the 1% level."
              }
            }
          ],
          "inner": []
        }
      }
    ],
    "title": null
  },
  "see_also": [
    {
      "name": {
        "name": "Generator.f",
        "ref": null,
        "exists": null
      },
      "descriptions": [
        {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "which should be used for new code."
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
        "name": "scipy.stats.f",
        "ref": null,
        "exists": null
      },
      "descriptions": [
        {
          "inline": [
            {
              "type": "Words",
              "data": {
                "value": "probability density function, distribution or cumulative density function, etc."
              }
            }
          ],
          "inner": []
        }
      ],
      "type": null
    }
  ],
  "version": "2021.10.0",
  "signature": "f(self, dfnum, dfden, size=None, chunks='auto', **kwargs)",
  "references": null,
  "logo": "logo.png",
  "qa": "dask.array.random.RandomState.f",
  "arbitrary": []
}