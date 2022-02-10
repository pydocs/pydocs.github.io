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
                  "value": "If the timestamps have a timezone, ceiling will take place relative to the local (\"wall\") time and re-localized to the same timezone. When ceiling near daylight savings time, use "
                }
              },
              {
                "type": "Verbatim",
                "data": {
                  "value": [
                    "nonexistent"
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
                    "ambiguous"
                  ]
                }
              },
              {
                "type": "Words",
                "data": {
                  "value": " to control the re-localization behavior."
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
            "param": "freq",
            "type_": "str or Offset",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "The frequency level to ceil the index to. Must be a fixed frequency like 'S' (second) not 'ME' (month end). See "
                      }
                    },
                    {
                      "type": "Directive",
                      "data": {
                        "value": "frequency aliases <timeseries.offset_aliases>",
                        "domain": null,
                        "role": "ref"
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " for a list of possible "
                      }
                    },
                    {
                      "type": "Link",
                      "data": {
                        "value": "freq",
                        "reference": {
                          "module": null,
                          "version": null,
                          "kind": "local",
                          "path": "freq"
                        },
                        "kind": "local",
                        "exists": true
                      }
                    },
                    {
                      "type": "Words",
                      "data": {
                        "value": " values."
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
            "param": "ambiguous",
            "type_": "'infer', bool-ndarray, 'NaT', default 'raise'",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Only relevant for DatetimeIndex:"
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
                              "value": "'infer' will attempt to infer fall dst-transition hours based on   order"
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
                              "value": "bool-ndarray where True signifies a DST time, False designates   a non-DST time (note that this flag is only applicable for   ambiguous times)"
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
                              "value": "'NaT' will return NaT where there are ambiguous times"
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
                              "value": "'raise' will raise an AmbiguousTimeError if there are ambiguous   times."
                            }
                          }
                        ],
                        "inner": []
                      }
                    }
                  ]
                }
              }
            ]
          }
        },
        {
          "type": "Param",
          "data": {
            "param": "nonexistent",
            "type_": "'shift_forward', 'shift_backward', 'NaT', timedelta, default 'raise'",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "A nonexistent time does not exist in a particular timezone where clocks moved forward due to DST."
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
                              "value": "'shift_forward' will shift the nonexistent time forward to the   closest existing time"
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
                              "value": "'shift_backward' will shift the nonexistent time backward to the   closest existing time"
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
                              "value": "'NaT' will return NaT where there are nonexistent times"
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
                              "value": "timedelta objects will shift nonexistent times by the timedelta"
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
                              "value": "'raise' will raise an NonExistentTimeError if there are   nonexistent times."
                            }
                          }
                        ],
                        "inner": []
                      }
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
      "children": [
        {
          "type": "Param",
          "data": {
            "param": "",
            "type_": "ValueError if the `freq` cannot be converted.",
            "desc": []
          }
        }
      ],
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
            "type_": "DatetimeIndex, TimedeltaIndex, or Series",
            "desc": [
              {
                "type": "Paragraph",
                "data": {
                  "inline": [
                    {
                      "type": "Words",
                      "data": {
                        "value": "Index of the same type for a DatetimeIndex or TimedeltaIndex, or a Series with the same index for a Series."
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
                  "value": "Perform ceil operation on the data to the specified "
                }
              },
              {
                "type": "Link",
                "data": {
                  "value": "freq",
                  "reference": {
                    "module": null,
                    "version": null,
                    "kind": "local",
                    "path": "freq"
                  },
                  "kind": "local",
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
      "path": "pandas.core.indexes.datetimes.date_range"
    },
    {
      "module": "pandas",
      "version": "1.4.0",
      "kind": "module",
      "path": "pandas.core.indexes.datetimes.DatetimeIndex"
    },
    {
      "module": "pandas",
      "version": "1.4.0",
      "kind": "module",
      "path": "pandas.core.series.Series"
    },
    {
      "module": "pandas",
      "version": "1.4.0",
      "kind": "module",
      "path": "pandas.core.arrays.datetimelike.validate_periods"
    }
  ],
  "ordered_sections": [
    "Summary",
    "Parameters",
    "Returns",
    "Raises",
    "Notes",
    "Examples"
  ],
  "item_file": "/pandas/core/accessor.py",
  "item_line": 93,
  "item_type": "<class 'function'>",
  "aliases": [
    "pandas.core.series.CategoricalAccessor.rename_categories",
    "pandas.core.series.CategoricalAccessor.reorder_categories",
    "pandas.core.series.CategoricalAccessor.add_categories",
    "pandas.core.series.CategoricalAccessor.remove_categories",
    "pandas.core.series.CategoricalAccessor.remove_unused_categories",
    "pandas.core.series.CategoricalAccessor.set_categories",
    "pandas.core.series.CategoricalAccessor.as_ordered",
    "pandas.core.series.CategoricalAccessor.as_unordered",
    "pandas.core.indexes.accessors.DatetimeProperties.to_period",
    "pandas.core.indexes.accessors.DatetimeProperties.tz_localize",
    "pandas.core.indexes.accessors.DatetimeProperties.tz_convert",
    "pandas.core.indexes.accessors.DatetimeProperties.normalize",
    "pandas.core.indexes.accessors.DatetimeProperties.strftime",
    "pandas.core.indexes.accessors.DatetimeProperties.round",
    "pandas.core.indexes.accessors.DatetimeProperties.floor",
    "pandas.core.indexes.accessors.DatetimeProperties.ceil",
    "pandas.core.indexes.accessors.DatetimeProperties.month_name",
    "pandas.core.indexes.accessors.DatetimeProperties.day_name",
    "pandas.core.indexes.accessors.PeriodProperties.strftime",
    "pandas.core.indexes.accessors.PeriodProperties.to_timestamp",
    "pandas.core.indexes.accessors.PeriodProperties.asfreq",
    "pandas.core.indexes.accessors.TimedeltaProperties.total_seconds",
    "pandas.core.indexes.accessors.TimedeltaProperties.round",
    "pandas.core.indexes.accessors.TimedeltaProperties.floor",
    "pandas.core.indexes.accessors.TimedeltaProperties.ceil"
  ],
  "example_section_data": {
    "children": [
      {
        "type": "Paragraph",
        "data": {
          "inline": [
            {
              "type": "Strong",
              "data": {
                "content": {
                  "value": "DatetimeIndex"
                }
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
                "data": "rng"
              }
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
                "data": "pd"
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
                  "value": "date_range",
                  "reference": {
                    "module": "pandas",
                    "version": "1.4.0",
                    "kind": "module",
                    "path": "pandas.core.indexes.datetimes.date_range"
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
                "data": "1/1/2018 11:59:00"
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
                "type": "Link",
                "data": {
                  "value": "periods",
                  "reference": {
                    "module": "pandas",
                    "version": "1.4.0",
                    "kind": "module",
                    "path": "pandas.core.arrays.datetimelike.validate_periods"
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
                "data": "="
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
                "data": "freq"
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
                "data": "min"
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
                "data": "rng"
              }
            }
          ],
          "out": "DatetimeIndex(['2018-01-01 11:59:00', '2018-01-01 12:00:00',\n               '2018-01-01 12:01:00'],\n              dtype='datetime64[ns]', freq='T')",
          "ce_status": "compiled"
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
                "data": "rng"
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
                "data": "ceil"
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
                "data": "H"
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
            }
          ],
          "out": "DatetimeIndex(['2018-01-01 12:00:00', '2018-01-01 12:00:00',\n               '2018-01-01 13:00:00'],\n              dtype='datetime64[ns]', freq=None)",
          "ce_status": "compiled"
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
                  "value": "Series"
                }
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
                "data": "pd"
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
                  "value": "Series",
                  "reference": {
                    "module": "pandas",
                    "version": "1.4.0",
                    "kind": "module",
                    "path": "pandas.core.series.Series"
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
                "data": "rng"
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
                "data": "dt"
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
                "data": "ceil"
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
                "data": "H"
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
                "data": ")"
              }
            }
          ],
          "out": "0   2018-01-01 12:00:00\n1   2018-01-01 12:00:00\n2   2018-01-01 13:00:00\ndtype: datetime64[ns]",
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
                "value": "When rounding near a daylight savings time transition, use "
              }
            },
            {
              "type": "Verbatim",
              "data": {
                "value": [
                  "ambiguous"
                ]
              }
            },
            {
              "type": "Words",
              "data": {
                "value": " or "
              }
            },
            {
              "type": "Verbatim",
              "data": {
                "value": [
                  "nonexistent"
                ]
              }
            },
            {
              "type": "Words",
              "data": {
                "value": " to control how the timestamp should be re-localized."
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
                "data": "rng_tz"
              }
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
                "data": "pd"
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
                  "value": "DatetimeIndex",
                  "reference": {
                    "module": "pandas",
                    "version": "1.4.0",
                    "kind": "module",
                    "path": "pandas.core.indexes.datetimes.DatetimeIndex"
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
                "data": "["
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
                "data": "2021-10-31 01:30:00"
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
                "data": "]"
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
                "data": "tz"
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
                "data": "Europe/Amsterdam"
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
                "data": ")"
              }
            }
          ],
          "out": "",
          "ce_status": "compiled"
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
                "data": "rng_tz"
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
                "data": "ceil"
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
                "data": "H"
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
                "data": "ambiguous"
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
                "data": "False"
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
          "out": "DatetimeIndex(['2021-10-31 02:00:00+01:00'],\n              dtype='datetime64[ns, Europe/Amsterdam]', freq=None)",
          "ce_status": "compiled"
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
                "data": "rng_tz"
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
                "data": "ceil"
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
                "data": "H"
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
                "data": "ambiguous"
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
            }
          ],
          "out": "DatetimeIndex(['2021-10-31 02:00:00+02:00'],\n              dtype='datetime64[ns, Europe/Amsterdam]', freq=None)",
          "ce_status": "compiled"
        }
      }
    ],
    "title": null
  },
  "see_also": [],
  "version": "1.4.0",
  "signature": "f(self, *args, **kwargs)",
  "references": null,
  "logo": "logo.png",
  "qa": "pandas.core.accessor.PandasDelegate._add_delegate_accessors.<locals>._create_delegator_method.<locals>.f",
  "arbitrary": []
}