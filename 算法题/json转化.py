from jsonmerge import merge, Merger
from pprint import pprint
A = {
  "ins_list": ["CZCE.SR701", "SHFE.cu1612"]
}
B = {
  "ins_list": ["SHFE.cu1612", "CZCE.SR701"],
  "quotes": {
    "CZCE.SR701": {
      "datetime": "2016-12-30 13:21:32.500000",
      "last_price": 6580.0
    },
    "SHFE.cu1612": {
      "datetime": "2016-12-30 13:21:31.500000",
      "last_price": 36440.0,
      "ask": [
        {
          "price": 36450.0,
          "volume": 12
        },
        {
          "price": 36460.0,
          "volume":2
        }
      ]
    }
  }
}
result1 = merge(A, B)
pprint(result1)

result2 = A.overwrite(B)
pprint(result2)

