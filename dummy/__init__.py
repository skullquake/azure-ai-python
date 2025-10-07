import json
import time
import azure.functions as func
import requests
import logging
import os
from typing import BinaryIO, Optional
import re
import base64
import io
import random
import string
################################################################################
# azure logging sample
################################################################################
logger = logging.getLogger('akshay')
logger.setLevel(logging.DEBUG)
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
logger.addHandler(sh)
logger.debug('Constructor:begin')
logger.debug('Constructor:end')
def main(req: func.HttpRequest) -> func.HttpResponse:
    logger.debug('--- DUMMY ---')
    logger.debug('--- Incoming request ---')
    logger.debug(f'Headers: {dict(req.headers)}')
    try:
        logger.debug(f'Body: {req.get_body().decode("utf-8", errors="replace")[:2048]}')
    except Exception as e:
        logger.debug(f'Body decode error: {e}')
    resp = {
      "status": "success",
      "message": "Request processed successfully.",
      "analyze_result": {
        "status": "succeeded",
        "createdDateTime": "2025-09-22T13:28:37Z",
        "lastUpdatedDateTime": "2025-09-22T13:28:37Z",
        "analyzeResult": {
          "apiVersion": "2024-11-30",
          "modelId": "prebuilt-invoice",
          "stringIndexType": "textElements",
          "content": "0987123654\nOriginal for Recipient\nContoso LTD\nWindsor tower, 123th Floor, Salsette Road\nTax Invoice\nContoso\nKalina, Santacruz East, Mumbai, Maharashtra\n400098 GSTIN: 12ABCDE0123A1A2\nMSFT0011223344\nPAN: ABCDE123F\nINVOICE TO\nMicrosoft Corporation India Pvt Ltd\nDATE\nPLEASE PAY\nDUE DATE\nLevel 10, Tower C, DLF Epitome Building No. 5, DLF\n31-12-2022\n₹ 6,54,321.00\n31-03-2023\nCyber City, Gurgaon 122002\nState Code:\n5\nGSTIN:\n98AAAAA7654Z3Z2\nPLACE OF SUPPLY:\n5\nMaharashtra\nS.NO\nDESCRIPTION\nHSN/SAC\nIGST\nSGST\nCGST\nAMOUNT\nPO# 99112233: IGNITE 2023 Posters, banners\n1\nand wristbands designs\n998877\n18%\n0%\n0%\n₹ 4,50,000.00\nPO# 99112233: INSPIRE 2023 Advertisement\n1\n112233\n18%\n0%\n0%\n₹ 1,50,000.00\ncampaign consulting service\nAccount Name: Contoso LTD\nSUBTOTAL\n₹ 6,00,000.00\nIFS CODE: CTS0011223\nIGST\n₹ 1,08,000.00\nSwift Code: MSFTINB123\nSGST\n₹ 0.00\nAccount Number: 998877665544332\nCGST\n₹ 0.00\nAddress: Contoso Bank LTD, 1 Linking road\nTotal\n₹ 7,08,000.00\nKhar West, Mumbai, Maharashtra 400052\nAdvance\n₹ 0.00\nIndia\nTOTAL DUE\n₹ 7,08,000.00\nTHANK YOU.",
          "pages": [
            {
              "pageNumber": 1,
              "angle": 0.025186950340867043,
              "width": 1200,
              "height": 893,
              "unit": "pixel",
              "words": [
                {
                  "content": "0987123654",
                  "polygon": [
                    286,
                    3,
                    407,
                    3,
                    407,
                    22,
                    286,
                    22
                  ],
                  "confidence": 0.995,
                  "span": {
                    "offset": 0,
                    "length": 10
                  }
                },
                {
                  "content": "Original",
                  "polygon": [
                    550,
                    25,
                    586,
                    25,
                    586,
                    37,
                    550,
                    36
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 11,
                    "length": 8
                  }
                },
                {
                  "content": "for",
                  "polygon": [
                    589,
                    25,
                    603,
                    25,
                    603,
                    37,
                    589,
                    37
                  ],
                  "confidence": 0.994,
                  "span": {
                    "offset": 20,
                    "length": 3
                  }
                },
                {
                  "content": "Recipient",
                  "polygon": [
                    605,
                    25,
                    649,
                    25,
                    649,
                    36,
                    605,
                    37
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 24,
                    "length": 9
                  }
                },
                {
                  "content": "Contoso",
                  "polygon": [
                    305,
                    101,
                    342,
                    100,
                    342,
                    110,
                    305,
                    110
                  ],
                  "confidence": 0.995,
                  "span": {
                    "offset": 34,
                    "length": 7
                  }
                },
                {
                  "content": "LTD",
                  "polygon": [
                    345,
                    100,
                    363,
                    100,
                    363,
                    110,
                    345,
                    110
                  ],
                  "confidence": 0.996,
                  "span": {
                    "offset": 42,
                    "length": 3
                  }
                },
                {
                  "content": "Windsor",
                  "polygon": [
                    304,
                    118,
                    341,
                    118,
                    341,
                    129,
                    304,
                    129
                  ],
                  "confidence": 0.994,
                  "span": {
                    "offset": 46,
                    "length": 7
                  }
                },
                {
                  "content": "tower,",
                  "polygon": [
                    343,
                    118,
                    370,
                    118,
                    370,
                    129,
                    343,
                    129
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 54,
                    "length": 6
                  }
                },
                {
                  "content": "123th",
                  "polygon": [
                    372,
                    118,
                    396,
                    118,
                    396,
                    129,
                    373,
                    129
                  ],
                  "confidence": 0.993,
                  "span": {
                    "offset": 61,
                    "length": 5
                  }
                },
                {
                  "content": "Floor,",
                  "polygon": [
                    399,
                    118,
                    423,
                    118,
                    423,
                    129,
                    399,
                    129
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 67,
                    "length": 6
                  }
                },
                {
                  "content": "Salsette",
                  "polygon": [
                    426,
                    118,
                    460,
                    118,
                    460,
                    129,
                    426,
                    129
                  ],
                  "confidence": 0.995,
                  "span": {
                    "offset": 74,
                    "length": 8
                  }
                },
                {
                  "content": "Road",
                  "polygon": [
                    462,
                    118,
                    487,
                    118,
                    487,
                    129,
                    462,
                    129
                  ],
                  "confidence": 0.987,
                  "span": {
                    "offset": 83,
                    "length": 4
                  }
                },
                {
                  "content": "Tax",
                  "polygon": [
                    549,
                    115,
                    578,
                    115,
                    578,
                    131,
                    549,
                    131
                  ],
                  "confidence": 0.998,
                  "span": {
                    "offset": 88,
                    "length": 3
                  }
                },
                {
                  "content": "Invoice",
                  "polygon": [
                    583,
                    115,
                    641,
                    115,
                    641,
                    131,
                    584,
                    131
                  ],
                  "confidence": 0.99,
                  "span": {
                    "offset": 92,
                    "length": 7
                  }
                },
                {
                  "content": "Contoso",
                  "polygon": [
                    776,
                    122,
                    871,
                    124,
                    871,
                    150,
                    776,
                    153
                  ],
                  "confidence": 0.987,
                  "span": {
                    "offset": 100,
                    "length": 7
                  }
                },
                {
                  "content": "Kalina,",
                  "polygon": [
                    307,
                    136,
                    337,
                    136,
                    337,
                    147,
                    307,
                    147
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 108,
                    "length": 7
                  }
                },
                {
                  "content": "Santacruz",
                  "polygon": [
                    340,
                    136,
                    383,
                    136,
                    383,
                    147,
                    340,
                    147
                  ],
                  "confidence": 0.993,
                  "span": {
                    "offset": 116,
                    "length": 9
                  }
                },
                {
                  "content": "East,",
                  "polygon": [
                    385,
                    136,
                    406,
                    136,
                    406,
                    147,
                    385,
                    147
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 126,
                    "length": 5
                  }
                },
                {
                  "content": "Mumbai,",
                  "polygon": [
                    409,
                    136,
                    445,
                    136,
                    445,
                    147,
                    409,
                    147
                  ],
                  "confidence": 0.986,
                  "span": {
                    "offset": 132,
                    "length": 7
                  }
                },
                {
                  "content": "Maharashtra",
                  "polygon": [
                    448,
                    136,
                    503,
                    136,
                    503,
                    147,
                    448,
                    147
                  ],
                  "confidence": 0.994,
                  "span": {
                    "offset": 140,
                    "length": 11
                  }
                },
                {
                  "content": "400098",
                  "polygon": [
                    305,
                    154,
                    335,
                    154,
                    335,
                    164,
                    305,
                    164
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 152,
                    "length": 6
                  }
                },
                {
                  "content": "GSTIN:",
                  "polygon": [
                    340,
                    154,
                    370,
                    154,
                    370,
                    164,
                    340,
                    164
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 159,
                    "length": 6
                  }
                },
                {
                  "content": "12ABCDE0123A1A2",
                  "polygon": [
                    373,
                    154,
                    460,
                    154,
                    460,
                    164,
                    373,
                    164
                  ],
                  "confidence": 0.989,
                  "span": {
                    "offset": 166,
                    "length": 15
                  }
                },
                {
                  "content": "MSFT0011223344",
                  "polygon": [
                    532,
                    146,
                    678,
                    146,
                    678,
                    162,
                    532,
                    162
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 182,
                    "length": 14
                  }
                },
                {
                  "content": "PAN:",
                  "polygon": [
                    304,
                    172,
                    327,
                    172,
                    327,
                    182,
                    304,
                    182
                  ],
                  "confidence": 0.934,
                  "span": {
                    "offset": 197,
                    "length": 4
                  }
                },
                {
                  "content": "ABCDE123F",
                  "polygon": [
                    329,
                    172,
                    383,
                    172,
                    383,
                    182,
                    329,
                    182
                  ],
                  "confidence": 0.79,
                  "span": {
                    "offset": 202,
                    "length": 9
                  }
                },
                {
                  "content": "INVOICE",
                  "polygon": [
                    304,
                    186,
                    346,
                    186,
                    346,
                    196,
                    304,
                    196
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 212,
                    "length": 7
                  }
                },
                {
                  "content": "TO",
                  "polygon": [
                    348,
                    186,
                    363,
                    186,
                    363,
                    196,
                    348,
                    196
                  ],
                  "confidence": 0.996,
                  "span": {
                    "offset": 220,
                    "length": 2
                  }
                },
                {
                  "content": "Microsoft",
                  "polygon": [
                    304,
                    204,
                    353,
                    204,
                    353,
                    216,
                    304,
                    216
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 223,
                    "length": 9
                  }
                },
                {
                  "content": "Corporation",
                  "polygon": [
                    355,
                    204,
                    411,
                    204,
                    411,
                    216,
                    355,
                    216
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 233,
                    "length": 11
                  }
                },
                {
                  "content": "India",
                  "polygon": [
                    413,
                    204,
                    439,
                    204,
                    439,
                    216,
                    413,
                    216
                  ],
                  "confidence": 0.986,
                  "span": {
                    "offset": 245,
                    "length": 5
                  }
                },
                {
                  "content": "Pvt",
                  "polygon": [
                    442,
                    204,
                    458,
                    204,
                    458,
                    216,
                    442,
                    216
                  ],
                  "confidence": 0.562,
                  "span": {
                    "offset": 251,
                    "length": 3
                  }
                },
                {
                  "content": "Ltd",
                  "polygon": [
                    460,
                    204,
                    477,
                    204,
                    477,
                    216,
                    460,
                    216
                  ],
                  "confidence": 0.99,
                  "span": {
                    "offset": 255,
                    "length": 3
                  }
                },
                {
                  "content": "DATE",
                  "polygon": [
                    602,
                    205,
                    629,
                    205,
                    629,
                    215,
                    602,
                    215
                  ],
                  "confidence": 0.991,
                  "span": {
                    "offset": 259,
                    "length": 4
                  }
                },
                {
                  "content": "PLEASE",
                  "polygon": [
                    689,
                    204,
                    727,
                    204,
                    727,
                    215,
                    689,
                    215
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 264,
                    "length": 6
                  }
                },
                {
                  "content": "PAY",
                  "polygon": [
                    730,
                    204,
                    751,
                    204,
                    751,
                    215,
                    730,
                    215
                  ],
                  "confidence": 0.998,
                  "span": {
                    "offset": 271,
                    "length": 3
                  }
                },
                {
                  "content": "DUE",
                  "polygon": [
                    797,
                    204,
                    818,
                    204,
                    818,
                    215,
                    797,
                    215
                  ],
                  "confidence": 0.998,
                  "span": {
                    "offset": 275,
                    "length": 3
                  }
                },
                {
                  "content": "DATE",
                  "polygon": [
                    821,
                    204,
                    848,
                    204,
                    848,
                    215,
                    821,
                    215
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 279,
                    "length": 4
                  }
                },
                {
                  "content": "Level",
                  "polygon": [
                    304,
                    224,
                    331,
                    224,
                    331,
                    237,
                    304,
                    236
                  ],
                  "confidence": 0.994,
                  "span": {
                    "offset": 284,
                    "length": 5
                  }
                },
                {
                  "content": "10,",
                  "polygon": [
                    334,
                    224,
                    348,
                    224,
                    348,
                    237,
                    334,
                    237
                  ],
                  "confidence": 0.989,
                  "span": {
                    "offset": 290,
                    "length": 3
                  }
                },
                {
                  "content": "Tower",
                  "polygon": [
                    351,
                    224,
                    381,
                    224,
                    381,
                    237,
                    351,
                    237
                  ],
                  "confidence": 0.996,
                  "span": {
                    "offset": 294,
                    "length": 5
                  }
                },
                {
                  "content": "C,",
                  "polygon": [
                    383,
                    224,
                    393,
                    224,
                    393,
                    237,
                    383,
                    237
                  ],
                  "confidence": 0.977,
                  "span": {
                    "offset": 300,
                    "length": 2
                  }
                },
                {
                  "content": "DLF",
                  "polygon": [
                    396,
                    224,
                    414,
                    224,
                    414,
                    237,
                    395,
                    237
                  ],
                  "confidence": 0.995,
                  "span": {
                    "offset": 303,
                    "length": 3
                  }
                },
                {
                  "content": "Epitome",
                  "polygon": [
                    417,
                    224,
                    457,
                    224,
                    457,
                    237,
                    417,
                    237
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 307,
                    "length": 7
                  }
                },
                {
                  "content": "Building",
                  "polygon": [
                    460,
                    224,
                    498,
                    224,
                    498,
                    237,
                    460,
                    237
                  ],
                  "confidence": 0.989,
                  "span": {
                    "offset": 315,
                    "length": 8
                  }
                },
                {
                  "content": "No.",
                  "polygon": [
                    500,
                    224,
                    518,
                    224,
                    518,
                    237,
                    500,
                    237
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 324,
                    "length": 3
                  }
                },
                {
                  "content": "5,",
                  "polygon": [
                    521,
                    224,
                    530,
                    224,
                    530,
                    237,
                    521,
                    237
                  ],
                  "confidence": 0.99,
                  "span": {
                    "offset": 328,
                    "length": 2
                  }
                },
                {
                  "content": "DLF",
                  "polygon": [
                    533,
                    224,
                    552,
                    224,
                    552,
                    237,
                    533,
                    237
                  ],
                  "confidence": 0.995,
                  "span": {
                    "offset": 331,
                    "length": 3
                  }
                },
                {
                  "content": "31-12-2022",
                  "polygon": [
                    585,
                    225,
                    646,
                    225,
                    646,
                    236,
                    585,
                    236
                  ],
                  "confidence": 0.994,
                  "span": {
                    "offset": 335,
                    "length": 10
                  }
                },
                {
                  "content": "₹",
                  "polygon": [
                    685,
                    225,
                    692,
                    225,
                    692,
                    236,
                    685,
                    236
                  ],
                  "confidence": 1,
                  "span": {
                    "offset": 346,
                    "length": 1
                  }
                },
                {
                  "content": "6,54,321.00",
                  "polygon": [
                    694,
                    225,
                    756,
                    225,
                    756,
                    236,
                    694,
                    236
                  ],
                  "confidence": 0.993,
                  "span": {
                    "offset": 348,
                    "length": 11
                  }
                },
                {
                  "content": "31-03-2023",
                  "polygon": [
                    793,
                    225,
                    855,
                    225,
                    855,
                    236,
                    793,
                    236
                  ],
                  "confidence": 0.994,
                  "span": {
                    "offset": 360,
                    "length": 10
                  }
                },
                {
                  "content": "Cyber",
                  "polygon": [
                    304,
                    244,
                    332,
                    244,
                    332,
                    257,
                    304,
                    257
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 371,
                    "length": 5
                  }
                },
                {
                  "content": "City,",
                  "polygon": [
                    334,
                    244,
                    357,
                    244,
                    357,
                    257,
                    334,
                    257
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 377,
                    "length": 5
                  }
                },
                {
                  "content": "Gurgaon",
                  "polygon": [
                    361,
                    244,
                    402,
                    244,
                    402,
                    257,
                    361,
                    257
                  ],
                  "confidence": 0.994,
                  "span": {
                    "offset": 383,
                    "length": 7
                  }
                },
                {
                  "content": "122002",
                  "polygon": [
                    406,
                    244,
                    444,
                    244,
                    444,
                    257,
                    406,
                    257
                  ],
                  "confidence": 0.995,
                  "span": {
                    "offset": 391,
                    "length": 6
                  }
                },
                {
                  "content": "State",
                  "polygon": [
                    355,
                    296,
                    382,
                    296,
                    382,
                    307,
                    355,
                    307
                  ],
                  "confidence": 0.997,
                  "span": {
                    "offset": 398,
                    "length": 5
                  }
                },
                {
                  "content": "Code:",
                  "polygon": [
                    384,
                    296,
                    413,
                    296,
                    413,
                    307,
                    384,
                    307
                  ],
                  "confidence": 0.997,
                  "span": {
                    "offset": 404,
                    "length": 5
                  }
                },
                {
                  "content": "5",
                  "polygon": [
                    548,
                    297,
                    556,
                    297,
                    556,
                    306,
                    547,
                    306
                  ],
                  "confidence": 0.995,
                  "span": {
                    "offset": 410,
                    "length": 1
                  }
                },
                {
                  "content": "GSTIN:",
                  "polygon": [
                    378,
                    315,
                    412,
                    315,
                    412,
                    326,
                    378,
                    325
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 412,
                    "length": 6
                  }
                },
                {
                  "content": "98AAAAA7654Z3Z2",
                  "polygon": [
                    457,
                    315,
                    553,
                    315,
                    553,
                    325,
                    457,
                    325
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 419,
                    "length": 15
                  }
                },
                {
                  "content": "PLACE",
                  "polygon": [
                    320,
                    334,
                    351,
                    334,
                    351,
                    345,
                    320,
                    345
                  ],
                  "confidence": 0.994,
                  "span": {
                    "offset": 435,
                    "length": 5
                  }
                },
                {
                  "content": "OF",
                  "polygon": [
                    354,
                    334,
                    368,
                    334,
                    367,
                    345,
                    354,
                    345
                  ],
                  "confidence": 0.998,
                  "span": {
                    "offset": 441,
                    "length": 2
                  }
                },
                {
                  "content": "SUPPLY:",
                  "polygon": [
                    370,
                    334,
                    412,
                    334,
                    412,
                    345,
                    370,
                    345
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 444,
                    "length": 7
                  }
                },
                {
                  "content": "5",
                  "polygon": [
                    455,
                    336,
                    463,
                    336,
                    463,
                    345,
                    455,
                    345
                  ],
                  "confidence": 0.996,
                  "span": {
                    "offset": 452,
                    "length": 1
                  }
                },
                {
                  "content": "Maharashtra",
                  "polygon": [
                    483,
                    335,
                    557,
                    336,
                    557,
                    346,
                    483,
                    346
                  ],
                  "confidence": 0.993,
                  "span": {
                    "offset": 454,
                    "length": 11
                  }
                },
                {
                  "content": "S.NO",
                  "polygon": [
                    320,
                    383,
                    347,
                    383,
                    347,
                    394,
                    320,
                    394
                  ],
                  "confidence": 0.989,
                  "span": {
                    "offset": 466,
                    "length": 4
                  }
                },
                {
                  "content": "DESCRIPTION",
                  "polygon": [
                    438,
                    383,
                    503,
                    383,
                    503,
                    394,
                    438,
                    394
                  ],
                  "confidence": 0.987,
                  "span": {
                    "offset": 471,
                    "length": 11
                  }
                },
                {
                  "content": "HSN/SAC",
                  "polygon": [
                    624,
                    383,
                    671,
                    383,
                    671,
                    394,
                    624,
                    394
                  ],
                  "confidence": 0.993,
                  "span": {
                    "offset": 483,
                    "length": 7
                  }
                },
                {
                  "content": "IGST",
                  "polygon": [
                    684,
                    383,
                    709,
                    383,
                    709,
                    394,
                    684,
                    394
                  ],
                  "confidence": 0.988,
                  "span": {
                    "offset": 491,
                    "length": 4
                  }
                },
                {
                  "content": "SGST",
                  "polygon": [
                    729,
                    383,
                    756,
                    383,
                    756,
                    394,
                    729,
                    394
                  ],
                  "confidence": 0.989,
                  "span": {
                    "offset": 496,
                    "length": 4
                  }
                },
                {
                  "content": "CGST",
                  "polygon": [
                    769,
                    383,
                    796,
                    383,
                    796,
                    394,
                    769,
                    394
                  ],
                  "confidence": 0.988,
                  "span": {
                    "offset": 501,
                    "length": 4
                  }
                },
                {
                  "content": "AMOUNT",
                  "polygon": [
                    816,
                    383,
                    864,
                    383,
                    864,
                    394,
                    816,
                    394
                  ],
                  "confidence": 0.995,
                  "span": {
                    "offset": 506,
                    "length": 6
                  }
                },
                {
                  "content": "PO#",
                  "polygon": [
                    377,
                    416,
                    396,
                    416,
                    396,
                    427,
                    377,
                    427
                  ],
                  "confidence": 0.977,
                  "span": {
                    "offset": 513,
                    "length": 3
                  }
                },
                {
                  "content": "99112233:",
                  "polygon": [
                    399,
                    416,
                    444,
                    416,
                    444,
                    427,
                    399,
                    427
                  ],
                  "confidence": 0.962,
                  "span": {
                    "offset": 517,
                    "length": 9
                  }
                },
                {
                  "content": "IGNITE",
                  "polygon": [
                    448,
                    416,
                    478,
                    416,
                    478,
                    427,
                    448,
                    427
                  ],
                  "confidence": 0.962,
                  "span": {
                    "offset": 527,
                    "length": 6
                  }
                },
                {
                  "content": "2023",
                  "polygon": [
                    482,
                    416,
                    504,
                    416,
                    504,
                    427,
                    482,
                    427
                  ],
                  "confidence": 0.986,
                  "span": {
                    "offset": 534,
                    "length": 4
                  }
                },
                {
                  "content": "Posters,",
                  "polygon": [
                    506,
                    416,
                    538,
                    416,
                    538,
                    427,
                    506,
                    427
                  ],
                  "confidence": 0.989,
                  "span": {
                    "offset": 539,
                    "length": 8
                  }
                },
                {
                  "content": "banners",
                  "polygon": [
                    540,
                    416,
                    578,
                    416,
                    578,
                    427,
                    540,
                    427
                  ],
                  "confidence": 0.991,
                  "span": {
                    "offset": 548,
                    "length": 7
                  }
                },
                {
                  "content": "1",
                  "polygon": [
                    331,
                    426,
                    336,
                    426,
                    336,
                    435,
                    331,
                    435
                  ],
                  "confidence": 0.995,
                  "span": {
                    "offset": 556,
                    "length": 1
                  }
                },
                {
                  "content": "and",
                  "polygon": [
                    377,
                    434,
                    392,
                    434,
                    392,
                    444,
                    377,
                    444
                  ],
                  "confidence": 0.995,
                  "span": {
                    "offset": 558,
                    "length": 3
                  }
                },
                {
                  "content": "wristbands",
                  "polygon": [
                    394,
                    434,
                    440,
                    434,
                    440,
                    444,
                    394,
                    444
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 562,
                    "length": 10
                  }
                },
                {
                  "content": "designs",
                  "polygon": [
                    442,
                    434,
                    477,
                    434,
                    477,
                    445,
                    442,
                    445
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 573,
                    "length": 7
                  }
                },
                {
                  "content": "998877",
                  "polygon": [
                    629,
                    424,
                    665,
                    424,
                    665,
                    435,
                    629,
                    435
                  ],
                  "confidence": 0.996,
                  "span": {
                    "offset": 581,
                    "length": 6
                  }
                },
                {
                  "content": "18%",
                  "polygon": [
                    688,
                    425,
                    710,
                    425,
                    710,
                    435,
                    688,
                    435
                  ],
                  "confidence": 0.988,
                  "span": {
                    "offset": 588,
                    "length": 3
                  }
                },
                {
                  "content": "0%",
                  "polygon": [
                    735,
                    425,
                    752,
                    424,
                    752,
                    435,
                    735,
                    435
                  ],
                  "confidence": 0.963,
                  "span": {
                    "offset": 592,
                    "length": 2
                  }
                },
                {
                  "content": "0%",
                  "polygon": [
                    776,
                    425,
                    793,
                    425,
                    793,
                    435,
                    776,
                    435
                  ],
                  "confidence": 0.949,
                  "span": {
                    "offset": 595,
                    "length": 2
                  }
                },
                {
                  "content": "₹",
                  "polygon": [
                    815,
                    424,
                    820,
                    424,
                    820,
                    436,
                    815,
                    436
                  ],
                  "confidence": 0.993,
                  "span": {
                    "offset": 598,
                    "length": 1
                  }
                },
                {
                  "content": "4,50,000.00",
                  "polygon": [
                    823,
                    424,
                    879,
                    424,
                    879,
                    436,
                    823,
                    436
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 600,
                    "length": 11
                  }
                },
                {
                  "content": "PO#",
                  "polygon": [
                    376,
                    455,
                    396,
                    455,
                    396,
                    466,
                    376,
                    466
                  ],
                  "confidence": 0.984,
                  "span": {
                    "offset": 612,
                    "length": 3
                  }
                },
                {
                  "content": "99112233:",
                  "polygon": [
                    398,
                    455,
                    444,
                    455,
                    444,
                    467,
                    398,
                    466
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 616,
                    "length": 9
                  }
                },
                {
                  "content": "INSPIRE",
                  "polygon": [
                    448,
                    455,
                    486,
                    455,
                    486,
                    467,
                    448,
                    467
                  ],
                  "confidence": 0.99,
                  "span": {
                    "offset": 626,
                    "length": 7
                  }
                },
                {
                  "content": "2023",
                  "polygon": [
                    488,
                    455,
                    509,
                    455,
                    509,
                    467,
                    488,
                    467
                  ],
                  "confidence": 0.989,
                  "span": {
                    "offset": 634,
                    "length": 4
                  }
                },
                {
                  "content": "Advertisement",
                  "polygon": [
                    511,
                    455,
                    574,
                    455,
                    574,
                    467,
                    511,
                    467
                  ],
                  "confidence": 0.934,
                  "span": {
                    "offset": 639,
                    "length": 13
                  }
                },
                {
                  "content": "1",
                  "polygon": [
                    331,
                    465,
                    337,
                    465,
                    337,
                    474,
                    331,
                    474
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 653,
                    "length": 1
                  }
                },
                {
                  "content": "112233",
                  "polygon": [
                    630,
                    462,
                    665,
                    461,
                    665,
                    472,
                    630,
                    472
                  ],
                  "confidence": 0.998,
                  "span": {
                    "offset": 655,
                    "length": 6
                  }
                },
                {
                  "content": "18%",
                  "polygon": [
                    688,
                    462,
                    710,
                    462,
                    710,
                    472,
                    688,
                    472
                  ],
                  "confidence": 0.976,
                  "span": {
                    "offset": 662,
                    "length": 3
                  }
                },
                {
                  "content": "0%",
                  "polygon": [
                    735,
                    462,
                    753,
                    462,
                    753,
                    472,
                    735,
                    472
                  ],
                  "confidence": 0.983,
                  "span": {
                    "offset": 666,
                    "length": 2
                  }
                },
                {
                  "content": "0%",
                  "polygon": [
                    776,
                    462,
                    794,
                    462,
                    794,
                    472,
                    776,
                    472
                  ],
                  "confidence": 0.952,
                  "span": {
                    "offset": 669,
                    "length": 2
                  }
                },
                {
                  "content": "₹",
                  "polygon": [
                    815,
                    461,
                    822,
                    461,
                    822,
                    473,
                    815,
                    473
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 672,
                    "length": 1
                  }
                },
                {
                  "content": "1,50,000.00",
                  "polygon": [
                    824,
                    461,
                    879,
                    461,
                    879,
                    473,
                    824,
                    473
                  ],
                  "confidence": 0.994,
                  "span": {
                    "offset": 674,
                    "length": 11
                  }
                },
                {
                  "content": "campaign",
                  "polygon": [
                    377,
                    473,
                    418,
                    473,
                    418,
                    485,
                    377,
                    485
                  ],
                  "confidence": 0.993,
                  "span": {
                    "offset": 686,
                    "length": 8
                  }
                },
                {
                  "content": "consulting",
                  "polygon": [
                    420,
                    473,
                    462,
                    473,
                    462,
                    485,
                    420,
                    485
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 695,
                    "length": 10
                  }
                },
                {
                  "content": "service",
                  "polygon": [
                    464,
                    473,
                    496,
                    473,
                    496,
                    485,
                    464,
                    485
                  ],
                  "confidence": 0.906,
                  "span": {
                    "offset": 706,
                    "length": 7
                  }
                },
                {
                  "content": "Account",
                  "polygon": [
                    304,
                    595,
                    345,
                    595,
                    345,
                    607,
                    304,
                    606
                  ],
                  "confidence": 0.995,
                  "span": {
                    "offset": 714,
                    "length": 7
                  }
                },
                {
                  "content": "Name:",
                  "polygon": [
                    348,
                    595,
                    381,
                    595,
                    381,
                    606,
                    348,
                    607
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 722,
                    "length": 5
                  }
                },
                {
                  "content": "Contoso",
                  "polygon": [
                    383,
                    595,
                    421,
                    595,
                    421,
                    606,
                    383,
                    606
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 728,
                    "length": 7
                  }
                },
                {
                  "content": "LTD",
                  "polygon": [
                    423,
                    595,
                    444,
                    595,
                    444,
                    606,
                    423,
                    606
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 736,
                    "length": 3
                  }
                },
                {
                  "content": "SUBTOTAL",
                  "polygon": [
                    622,
                    595,
                    675,
                    595,
                    675,
                    606,
                    622,
                    606
                  ],
                  "confidence": 0.995,
                  "span": {
                    "offset": 740,
                    "length": 8
                  }
                },
                {
                  "content": "₹",
                  "polygon": [
                    809,
                    595,
                    816,
                    595,
                    816,
                    606,
                    809,
                    606
                  ],
                  "confidence": 0.979,
                  "span": {
                    "offset": 749,
                    "length": 1
                  }
                },
                {
                  "content": "6,00,000.00",
                  "polygon": [
                    818,
                    595,
                    878,
                    595,
                    878,
                    606,
                    818,
                    606
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 751,
                    "length": 11
                  }
                },
                {
                  "content": "IFS",
                  "polygon": [
                    304,
                    614,
                    321,
                    614,
                    321,
                    625,
                    304,
                    625
                  ],
                  "confidence": 0.995,
                  "span": {
                    "offset": 763,
                    "length": 3
                  }
                },
                {
                  "content": "CODE:",
                  "polygon": [
                    324,
                    614,
                    357,
                    614,
                    357,
                    625,
                    324,
                    625
                  ],
                  "confidence": 0.996,
                  "span": {
                    "offset": 767,
                    "length": 5
                  }
                },
                {
                  "content": "CTS0011223",
                  "polygon": [
                    359,
                    614,
                    421,
                    614,
                    421,
                    625,
                    359,
                    625
                  ],
                  "confidence": 0.993,
                  "span": {
                    "offset": 773,
                    "length": 10
                  }
                },
                {
                  "content": "IGST",
                  "polygon": [
                    622,
                    613,
                    646,
                    613,
                    646,
                    623,
                    622,
                    623
                  ],
                  "confidence": 0.991,
                  "span": {
                    "offset": 784,
                    "length": 4
                  }
                },
                {
                  "content": "₹",
                  "polygon": [
                    809,
                    613,
                    816,
                    613,
                    816,
                    625,
                    809,
                    625
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 789,
                    "length": 1
                  }
                },
                {
                  "content": "1,08,000.00",
                  "polygon": [
                    818,
                    613,
                    878,
                    613,
                    878,
                    625,
                    818,
                    625
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 791,
                    "length": 11
                  }
                },
                {
                  "content": "Swift",
                  "polygon": [
                    305,
                    633,
                    330,
                    633,
                    330,
                    645,
                    305,
                    645
                  ],
                  "confidence": 0.995,
                  "span": {
                    "offset": 803,
                    "length": 5
                  }
                },
                {
                  "content": "Code:",
                  "polygon": [
                    332,
                    633,
                    361,
                    633,
                    361,
                    645,
                    332,
                    645
                  ],
                  "confidence": 0.993,
                  "span": {
                    "offset": 809,
                    "length": 5
                  }
                },
                {
                  "content": "MSFTINB123",
                  "polygon": [
                    364,
                    633,
                    428,
                    633,
                    428,
                    645,
                    364,
                    645
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 815,
                    "length": 10
                  }
                },
                {
                  "content": "SGST",
                  "polygon": [
                    622,
                    632,
                    649,
                    632,
                    649,
                    643,
                    622,
                    643
                  ],
                  "confidence": 0.989,
                  "span": {
                    "offset": 826,
                    "length": 4
                  }
                },
                {
                  "content": "₹",
                  "polygon": [
                    846,
                    632,
                    853,
                    632,
                    853,
                    643,
                    846,
                    643
                  ],
                  "confidence": 0.977,
                  "span": {
                    "offset": 831,
                    "length": 1
                  }
                },
                {
                  "content": "0.00",
                  "polygon": [
                    855,
                    632,
                    877,
                    632,
                    877,
                    643,
                    855,
                    643
                  ],
                  "confidence": 0.984,
                  "span": {
                    "offset": 833,
                    "length": 4
                  }
                },
                {
                  "content": "Account",
                  "polygon": [
                    305,
                    653,
                    347,
                    653,
                    347,
                    665,
                    305,
                    665
                  ],
                  "confidence": 0.993,
                  "span": {
                    "offset": 838,
                    "length": 7
                  }
                },
                {
                  "content": "Number:",
                  "polygon": [
                    349,
                    653,
                    391,
                    653,
                    391,
                    665,
                    349,
                    665
                  ],
                  "confidence": 0.993,
                  "span": {
                    "offset": 846,
                    "length": 7
                  }
                },
                {
                  "content": "998877665544332",
                  "polygon": [
                    394,
                    653,
                    482,
                    653,
                    482,
                    665,
                    394,
                    665
                  ],
                  "confidence": 0.993,
                  "span": {
                    "offset": 854,
                    "length": 15
                  }
                },
                {
                  "content": "CGST",
                  "polygon": [
                    622,
                    651,
                    649,
                    651,
                    649,
                    662,
                    622,
                    662
                  ],
                  "confidence": 0.988,
                  "span": {
                    "offset": 870,
                    "length": 4
                  }
                },
                {
                  "content": "₹",
                  "polygon": [
                    846,
                    651,
                    852,
                    651,
                    852,
                    662,
                    846,
                    662
                  ],
                  "confidence": 0.977,
                  "span": {
                    "offset": 875,
                    "length": 1
                  }
                },
                {
                  "content": "0.00",
                  "polygon": [
                    855,
                    651,
                    878,
                    651,
                    878,
                    662,
                    855,
                    662
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 877,
                    "length": 4
                  }
                },
                {
                  "content": "Address:",
                  "polygon": [
                    305,
                    672,
                    350,
                    672,
                    350,
                    684,
                    305,
                    684
                  ],
                  "confidence": 0.994,
                  "span": {
                    "offset": 882,
                    "length": 8
                  }
                },
                {
                  "content": "Contoso",
                  "polygon": [
                    352,
                    672,
                    391,
                    672,
                    391,
                    685,
                    352,
                    684
                  ],
                  "confidence": 0.995,
                  "span": {
                    "offset": 891,
                    "length": 7
                  }
                },
                {
                  "content": "Bank",
                  "polygon": [
                    393,
                    672,
                    415,
                    672,
                    415,
                    685,
                    393,
                    685
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 899,
                    "length": 4
                  }
                },
                {
                  "content": "LTD,",
                  "polygon": [
                    418,
                    672,
                    440,
                    672,
                    440,
                    685,
                    418,
                    685
                  ],
                  "confidence": 0.987,
                  "span": {
                    "offset": 904,
                    "length": 4
                  }
                },
                {
                  "content": "1",
                  "polygon": [
                    443,
                    672,
                    447,
                    672,
                    447,
                    685,
                    442,
                    685
                  ],
                  "confidence": 0.993,
                  "span": {
                    "offset": 909,
                    "length": 1
                  }
                },
                {
                  "content": "Linking",
                  "polygon": [
                    451,
                    672,
                    481,
                    672,
                    481,
                    685,
                    451,
                    685
                  ],
                  "confidence": 0.994,
                  "span": {
                    "offset": 911,
                    "length": 7
                  }
                },
                {
                  "content": "road",
                  "polygon": [
                    483,
                    672,
                    507,
                    672,
                    507,
                    685,
                    483,
                    685
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 919,
                    "length": 4
                  }
                },
                {
                  "content": "Total",
                  "polygon": [
                    622,
                    671,
                    649,
                    671,
                    649,
                    681,
                    622,
                    681
                  ],
                  "confidence": 0.996,
                  "span": {
                    "offset": 924,
                    "length": 5
                  }
                },
                {
                  "content": "₹",
                  "polygon": [
                    809,
                    670,
                    816,
                    670,
                    816,
                    681,
                    809,
                    681
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 930,
                    "length": 1
                  }
                },
                {
                  "content": "7,08,000.00",
                  "polygon": [
                    818,
                    670,
                    878,
                    669,
                    878,
                    681,
                    818,
                    681
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 932,
                    "length": 11
                  }
                },
                {
                  "content": "Khar",
                  "polygon": [
                    304,
                    692,
                    326,
                    692,
                    326,
                    704,
                    304,
                    704
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 944,
                    "length": 4
                  }
                },
                {
                  "content": "West,",
                  "polygon": [
                    328,
                    692,
                    355,
                    692,
                    355,
                    704,
                    328,
                    704
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 949,
                    "length": 5
                  }
                },
                {
                  "content": "Mumbai,",
                  "polygon": [
                    358,
                    692,
                    395,
                    692,
                    395,
                    704,
                    358,
                    704
                  ],
                  "confidence": 0.977,
                  "span": {
                    "offset": 955,
                    "length": 7
                  }
                },
                {
                  "content": "Maharashtra",
                  "polygon": [
                    398,
                    692,
                    456,
                    692,
                    456,
                    704,
                    398,
                    704
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 963,
                    "length": 11
                  }
                },
                {
                  "content": "400052",
                  "polygon": [
                    458,
                    692,
                    495,
                    692,
                    495,
                    704,
                    458,
                    704
                  ],
                  "confidence": 0.996,
                  "span": {
                    "offset": 975,
                    "length": 6
                  }
                },
                {
                  "content": "Advance",
                  "polygon": [
                    622,
                    689,
                    665,
                    689,
                    665,
                    700,
                    622,
                    700
                  ],
                  "confidence": 0.995,
                  "span": {
                    "offset": 982,
                    "length": 7
                  }
                },
                {
                  "content": "₹",
                  "polygon": [
                    846,
                    689,
                    853,
                    689,
                    853,
                    699,
                    846,
                    699
                  ],
                  "confidence": 0.993,
                  "span": {
                    "offset": 990,
                    "length": 1
                  }
                },
                {
                  "content": "0.00",
                  "polygon": [
                    855,
                    689,
                    878,
                    688,
                    878,
                    699,
                    855,
                    699
                  ],
                  "confidence": 0.992,
                  "span": {
                    "offset": 992,
                    "length": 4
                  }
                },
                {
                  "content": "India",
                  "polygon": [
                    305,
                    712,
                    329,
                    712,
                    329,
                    722,
                    305,
                    722
                  ],
                  "confidence": 0.963,
                  "span": {
                    "offset": 997,
                    "length": 5
                  }
                },
                {
                  "content": "TOTAL",
                  "polygon": [
                    623,
                    710,
                    675,
                    710,
                    675,
                    726,
                    623,
                    726
                  ],
                  "confidence": 0.996,
                  "span": {
                    "offset": 1003,
                    "length": 5
                  }
                },
                {
                  "content": "DUE",
                  "polygon": [
                    680,
                    710,
                    714,
                    710,
                    714,
                    726,
                    680,
                    726
                  ],
                  "confidence": 0.998,
                  "span": {
                    "offset": 1009,
                    "length": 3
                  }
                },
                {
                  "content": "₹",
                  "polygon": [
                    790,
                    709,
                    798,
                    709,
                    798,
                    722,
                    790,
                    722
                  ],
                  "confidence": 0.993,
                  "span": {
                    "offset": 1013,
                    "length": 1
                  }
                },
                {
                  "content": "7,08,000.00",
                  "polygon": [
                    801,
                    709,
                    877,
                    709,
                    877,
                    722,
                    801,
                    722
                  ],
                  "confidence": 0.995,
                  "span": {
                    "offset": 1015,
                    "length": 11
                  }
                },
                {
                  "content": "THANK",
                  "polygon": [
                    789,
                    739,
                    837,
                    739,
                    837,
                    755,
                    789,
                    755
                  ],
                  "confidence": 0.998,
                  "span": {
                    "offset": 1027,
                    "length": 5
                  }
                },
                {
                  "content": "YOU.",
                  "polygon": [
                    842,
                    739,
                    877,
                    739,
                    877,
                    755,
                    842,
                    755
                  ],
                  "confidence": 0.977,
                  "span": {
                    "offset": 1033,
                    "length": 4
                  }
                }
              ],
              "lines": [
                {
                  "content": "0987123654",
                  "polygon": [
                    286,
                    2,
                    406,
                    3,
                    406,
                    21,
                    286,
                    21
                  ],
                  "spans": [
                    {
                      "offset": 0,
                      "length": 10
                    }
                  ]
                },
                {
                  "content": "Original for Recipient",
                  "polygon": [
                    550,
                    25,
                    649,
                    25,
                    649,
                    36,
                    550,
                    36
                  ],
                  "spans": [
                    {
                      "offset": 11,
                      "length": 22
                    }
                  ]
                },
                {
                  "content": "Contoso LTD",
                  "polygon": [
                    305,
                    101,
                    362,
                    100,
                    362,
                    110,
                    305,
                    110
                  ],
                  "spans": [
                    {
                      "offset": 34,
                      "length": 11
                    }
                  ]
                },
                {
                  "content": "Windsor tower, 123th Floor, Salsette Road",
                  "polygon": [
                    304,
                    118,
                    486,
                    118,
                    486,
                    129,
                    304,
                    129
                  ],
                  "spans": [
                    {
                      "offset": 46,
                      "length": 41
                    }
                  ]
                },
                {
                  "content": "Tax Invoice",
                  "polygon": [
                    549,
                    115,
                    640,
                    115,
                    640,
                    131,
                    549,
                    131
                  ],
                  "spans": [
                    {
                      "offset": 88,
                      "length": 11
                    }
                  ]
                },
                {
                  "content": "Contoso",
                  "polygon": [
                    776,
                    122,
                    870,
                    121,
                    870,
                    152,
                    776,
                    152
                  ],
                  "spans": [
                    {
                      "offset": 100,
                      "length": 7
                    }
                  ]
                },
                {
                  "content": "Kalina, Santacruz East, Mumbai, Maharashtra",
                  "polygon": [
                    307,
                    136,
                    503,
                    136,
                    503,
                    147,
                    307,
                    147
                  ],
                  "spans": [
                    {
                      "offset": 108,
                      "length": 43
                    }
                  ]
                },
                {
                  "content": "400098 GSTIN: 12ABCDE0123A1A2",
                  "polygon": [
                    305,
                    154,
                    459,
                    154,
                    459,
                    164,
                    305,
                    164
                  ],
                  "spans": [
                    {
                      "offset": 152,
                      "length": 29
                    }
                  ]
                },
                {
                  "content": "MSFT0011223344",
                  "polygon": [
                    532,
                    146,
                    678,
                    146,
                    678,
                    162,
                    532,
                    162
                  ],
                  "spans": [
                    {
                      "offset": 182,
                      "length": 14
                    }
                  ]
                },
                {
                  "content": "PAN: ABCDE123F",
                  "polygon": [
                    304,
                    172,
                    382,
                    172,
                    382,
                    182,
                    304,
                    182
                  ],
                  "spans": [
                    {
                      "offset": 197,
                      "length": 14
                    }
                  ]
                },
                {
                  "content": "INVOICE TO",
                  "polygon": [
                    304,
                    186,
                    362,
                    186,
                    362,
                    196,
                    304,
                    196
                  ],
                  "spans": [
                    {
                      "offset": 212,
                      "length": 10
                    }
                  ]
                },
                {
                  "content": "Microsoft Corporation India Pvt Ltd",
                  "polygon": [
                    304,
                    204,
                    477,
                    204,
                    477,
                    216,
                    304,
                    216
                  ],
                  "spans": [
                    {
                      "offset": 223,
                      "length": 35
                    }
                  ]
                },
                {
                  "content": "DATE",
                  "polygon": [
                    602,
                    205,
                    629,
                    205,
                    629,
                    215,
                    602,
                    215
                  ],
                  "spans": [
                    {
                      "offset": 259,
                      "length": 4
                    }
                  ]
                },
                {
                  "content": "PLEASE PAY",
                  "polygon": [
                    689,
                    204,
                    751,
                    204,
                    751,
                    215,
                    689,
                    215
                  ],
                  "spans": [
                    {
                      "offset": 264,
                      "length": 10
                    }
                  ]
                },
                {
                  "content": "DUE DATE",
                  "polygon": [
                    797,
                    204,
                    848,
                    204,
                    848,
                    215,
                    797,
                    215
                  ],
                  "spans": [
                    {
                      "offset": 275,
                      "length": 8
                    }
                  ]
                },
                {
                  "content": "Level 10, Tower C, DLF Epitome Building No. 5, DLF",
                  "polygon": [
                    304,
                    224,
                    552,
                    224,
                    552,
                    237,
                    304,
                    237
                  ],
                  "spans": [
                    {
                      "offset": 284,
                      "length": 50
                    }
                  ]
                },
                {
                  "content": "31-12-2022",
                  "polygon": [
                    585,
                    225,
                    646,
                    225,
                    646,
                    236,
                    585,
                    236
                  ],
                  "spans": [
                    {
                      "offset": 335,
                      "length": 10
                    }
                  ]
                },
                {
                  "content": "₹ 6,54,321.00",
                  "polygon": [
                    685,
                    225,
                    756,
                    225,
                    755,
                    236,
                    685,
                    235
                  ],
                  "spans": [
                    {
                      "offset": 346,
                      "length": 13
                    }
                  ]
                },
                {
                  "content": "31-03-2023",
                  "polygon": [
                    793,
                    225,
                    854,
                    225,
                    854,
                    236,
                    793,
                    236
                  ],
                  "spans": [
                    {
                      "offset": 360,
                      "length": 10
                    }
                  ]
                },
                {
                  "content": "Cyber City, Gurgaon 122002",
                  "polygon": [
                    304,
                    244,
                    443,
                    244,
                    444,
                    257,
                    304,
                    257
                  ],
                  "spans": [
                    {
                      "offset": 371,
                      "length": 26
                    }
                  ]
                },
                {
                  "content": "State Code:",
                  "polygon": [
                    355,
                    296,
                    412,
                    296,
                    412,
                    307,
                    355,
                    307
                  ],
                  "spans": [
                    {
                      "offset": 398,
                      "length": 11
                    }
                  ]
                },
                {
                  "content": "5",
                  "polygon": [
                    548,
                    297,
                    555,
                    297,
                    555,
                    306,
                    547,
                    306
                  ],
                  "spans": [
                    {
                      "offset": 410,
                      "length": 1
                    }
                  ]
                },
                {
                  "content": "GSTIN:",
                  "polygon": [
                    378,
                    315,
                    412,
                    315,
                    412,
                    325,
                    378,
                    325
                  ],
                  "spans": [
                    {
                      "offset": 412,
                      "length": 6
                    }
                  ]
                },
                {
                  "content": "98AAAAA7654Z3Z2",
                  "polygon": [
                    457,
                    315,
                    553,
                    315,
                    553,
                    325,
                    457,
                    325
                  ],
                  "spans": [
                    {
                      "offset": 419,
                      "length": 15
                    }
                  ]
                },
                {
                  "content": "PLACE OF SUPPLY:",
                  "polygon": [
                    320,
                    334,
                    412,
                    334,
                    412,
                    345,
                    320,
                    345
                  ],
                  "spans": [
                    {
                      "offset": 435,
                      "length": 16
                    }
                  ]
                },
                {
                  "content": "5",
                  "polygon": [
                    455,
                    336,
                    463,
                    336,
                    463,
                    345,
                    455,
                    345
                  ],
                  "spans": [
                    {
                      "offset": 452,
                      "length": 1
                    }
                  ]
                },
                {
                  "content": "Maharashtra",
                  "polygon": [
                    483,
                    335,
                    556,
                    336,
                    556,
                    346,
                    483,
                    346
                  ],
                  "spans": [
                    {
                      "offset": 454,
                      "length": 11
                    }
                  ]
                },
                {
                  "content": "S.NO",
                  "polygon": [
                    320,
                    383,
                    346,
                    383,
                    346,
                    394,
                    320,
                    394
                  ],
                  "spans": [
                    {
                      "offset": 466,
                      "length": 4
                    }
                  ]
                },
                {
                  "content": "DESCRIPTION",
                  "polygon": [
                    438,
                    383,
                    503,
                    383,
                    503,
                    394,
                    438,
                    394
                  ],
                  "spans": [
                    {
                      "offset": 471,
                      "length": 11
                    }
                  ]
                },
                {
                  "content": "HSN/SAC",
                  "polygon": [
                    624,
                    383,
                    671,
                    383,
                    671,
                    394,
                    624,
                    394
                  ],
                  "spans": [
                    {
                      "offset": 483,
                      "length": 7
                    }
                  ]
                },
                {
                  "content": "IGST",
                  "polygon": [
                    684,
                    383,
                    708,
                    383,
                    708,
                    394,
                    684,
                    394
                  ],
                  "spans": [
                    {
                      "offset": 491,
                      "length": 4
                    }
                  ]
                },
                {
                  "content": "SGST",
                  "polygon": [
                    729,
                    383,
                    756,
                    383,
                    756,
                    394,
                    729,
                    394
                  ],
                  "spans": [
                    {
                      "offset": 496,
                      "length": 4
                    }
                  ]
                },
                {
                  "content": "CGST",
                  "polygon": [
                    769,
                    383,
                    796,
                    383,
                    796,
                    394,
                    769,
                    394
                  ],
                  "spans": [
                    {
                      "offset": 501,
                      "length": 4
                    }
                  ]
                },
                {
                  "content": "AMOUNT",
                  "polygon": [
                    816,
                    383,
                    863,
                    383,
                    863,
                    394,
                    816,
                    394
                  ],
                  "spans": [
                    {
                      "offset": 506,
                      "length": 6
                    }
                  ]
                },
                {
                  "content": "PO# 99112233: IGNITE 2023 Posters, banners",
                  "polygon": [
                    377,
                    416,
                    578,
                    416,
                    577,
                    427,
                    377,
                    427
                  ],
                  "spans": [
                    {
                      "offset": 513,
                      "length": 42
                    }
                  ]
                },
                {
                  "content": "1",
                  "polygon": [
                    331,
                    426,
                    336,
                    426,
                    336,
                    435,
                    331,
                    435
                  ],
                  "spans": [
                    {
                      "offset": 556,
                      "length": 1
                    }
                  ]
                },
                {
                  "content": "and wristbands designs",
                  "polygon": [
                    377,
                    433,
                    476,
                    434,
                    476,
                    445,
                    377,
                    444
                  ],
                  "spans": [
                    {
                      "offset": 558,
                      "length": 22
                    }
                  ]
                },
                {
                  "content": "998877",
                  "polygon": [
                    629,
                    424,
                    665,
                    424,
                    665,
                    435,
                    629,
                    435
                  ],
                  "spans": [
                    {
                      "offset": 581,
                      "length": 6
                    }
                  ]
                },
                {
                  "content": "18%",
                  "polygon": [
                    688,
                    425,
                    710,
                    425,
                    710,
                    435,
                    688,
                    435
                  ],
                  "spans": [
                    {
                      "offset": 588,
                      "length": 3
                    }
                  ]
                },
                {
                  "content": "0%",
                  "polygon": [
                    735,
                    425,
                    752,
                    424,
                    752,
                    435,
                    735,
                    435
                  ],
                  "spans": [
                    {
                      "offset": 592,
                      "length": 2
                    }
                  ]
                },
                {
                  "content": "0%",
                  "polygon": [
                    776,
                    425,
                    793,
                    425,
                    793,
                    435,
                    776,
                    435
                  ],
                  "spans": [
                    {
                      "offset": 595,
                      "length": 2
                    }
                  ]
                },
                {
                  "content": "₹ 4,50,000.00",
                  "polygon": [
                    815,
                    424,
                    879,
                    424,
                    879,
                    436,
                    815,
                    436
                  ],
                  "spans": [
                    {
                      "offset": 598,
                      "length": 13
                    }
                  ]
                },
                {
                  "content": "PO# 99112233: INSPIRE 2023 Advertisement",
                  "polygon": [
                    376,
                    455,
                    573,
                    455,
                    573,
                    467,
                    376,
                    466
                  ],
                  "spans": [
                    {
                      "offset": 612,
                      "length": 40
                    }
                  ]
                },
                {
                  "content": "1",
                  "polygon": [
                    331,
                    465,
                    336,
                    465,
                    336,
                    474,
                    331,
                    474
                  ],
                  "spans": [
                    {
                      "offset": 653,
                      "length": 1
                    }
                  ]
                },
                {
                  "content": "112233",
                  "polygon": [
                    630,
                    462,
                    664,
                    461,
                    664,
                    472,
                    630,
                    472
                  ],
                  "spans": [
                    {
                      "offset": 655,
                      "length": 6
                    }
                  ]
                },
                {
                  "content": "18%",
                  "polygon": [
                    688,
                    462,
                    710,
                    462,
                    710,
                    472,
                    688,
                    472
                  ],
                  "spans": [
                    {
                      "offset": 662,
                      "length": 3
                    }
                  ]
                },
                {
                  "content": "0%",
                  "polygon": [
                    735,
                    462,
                    752,
                    462,
                    752,
                    472,
                    735,
                    472
                  ],
                  "spans": [
                    {
                      "offset": 666,
                      "length": 2
                    }
                  ]
                },
                {
                  "content": "0%",
                  "polygon": [
                    776,
                    462,
                    793,
                    462,
                    793,
                    472,
                    776,
                    472
                  ],
                  "spans": [
                    {
                      "offset": 669,
                      "length": 2
                    }
                  ]
                },
                {
                  "content": "₹ 1,50,000.00",
                  "polygon": [
                    815,
                    461,
                    879,
                    461,
                    879,
                    473,
                    815,
                    473
                  ],
                  "spans": [
                    {
                      "offset": 672,
                      "length": 13
                    }
                  ]
                },
                {
                  "content": "campaign consulting service",
                  "polygon": [
                    377,
                    473,
                    495,
                    473,
                    495,
                    484,
                    377,
                    485
                  ],
                  "spans": [
                    {
                      "offset": 686,
                      "length": 27
                    }
                  ]
                },
                {
                  "content": "Account Name: Contoso LTD",
                  "polygon": [
                    304,
                    595,
                    444,
                    595,
                    444,
                    606,
                    304,
                    606
                  ],
                  "spans": [
                    {
                      "offset": 714,
                      "length": 25
                    }
                  ]
                },
                {
                  "content": "SUBTOTAL",
                  "polygon": [
                    622,
                    595,
                    675,
                    595,
                    675,
                    605,
                    622,
                    605
                  ],
                  "spans": [
                    {
                      "offset": 740,
                      "length": 8
                    }
                  ]
                },
                {
                  "content": "₹ 6,00,000.00",
                  "polygon": [
                    809,
                    595,
                    877,
                    595,
                    877,
                    606,
                    809,
                    606
                  ],
                  "spans": [
                    {
                      "offset": 749,
                      "length": 13
                    }
                  ]
                },
                {
                  "content": "IFS CODE: CTS0011223",
                  "polygon": [
                    304,
                    614,
                    421,
                    614,
                    421,
                    625,
                    304,
                    625
                  ],
                  "spans": [
                    {
                      "offset": 763,
                      "length": 20
                    }
                  ]
                },
                {
                  "content": "IGST",
                  "polygon": [
                    622,
                    613,
                    646,
                    613,
                    646,
                    623,
                    622,
                    623
                  ],
                  "spans": [
                    {
                      "offset": 784,
                      "length": 4
                    }
                  ]
                },
                {
                  "content": "₹ 1,08,000.00",
                  "polygon": [
                    809,
                    613,
                    877,
                    613,
                    877,
                    625,
                    809,
                    625
                  ],
                  "spans": [
                    {
                      "offset": 789,
                      "length": 13
                    }
                  ]
                },
                {
                  "content": "Swift Code: MSFTINB123",
                  "polygon": [
                    305,
                    633,
                    427,
                    633,
                    427,
                    645,
                    305,
                    645
                  ],
                  "spans": [
                    {
                      "offset": 803,
                      "length": 22
                    }
                  ]
                },
                {
                  "content": "SGST",
                  "polygon": [
                    622,
                    632,
                    648,
                    632,
                    648,
                    643,
                    622,
                    643
                  ],
                  "spans": [
                    {
                      "offset": 826,
                      "length": 4
                    }
                  ]
                },
                {
                  "content": "₹ 0.00",
                  "polygon": [
                    846,
                    632,
                    877,
                    632,
                    877,
                    643,
                    846,
                    643
                  ],
                  "spans": [
                    {
                      "offset": 831,
                      "length": 6
                    }
                  ]
                },
                {
                  "content": "Account Number: 998877665544332",
                  "polygon": [
                    305,
                    653,
                    481,
                    653,
                    481,
                    664,
                    305,
                    665
                  ],
                  "spans": [
                    {
                      "offset": 838,
                      "length": 31
                    }
                  ]
                },
                {
                  "content": "CGST",
                  "polygon": [
                    622,
                    651,
                    649,
                    651,
                    649,
                    662,
                    622,
                    662
                  ],
                  "spans": [
                    {
                      "offset": 870,
                      "length": 4
                    }
                  ]
                },
                {
                  "content": "₹ 0.00",
                  "polygon": [
                    846,
                    651,
                    877,
                    651,
                    877,
                    661,
                    846,
                    661
                  ],
                  "spans": [
                    {
                      "offset": 875,
                      "length": 6
                    }
                  ]
                },
                {
                  "content": "Address: Contoso Bank LTD, 1 Linking road",
                  "polygon": [
                    305,
                    672,
                    506,
                    672,
                    506,
                    685,
                    305,
                    684
                  ],
                  "spans": [
                    {
                      "offset": 882,
                      "length": 41
                    }
                  ]
                },
                {
                  "content": "Total",
                  "polygon": [
                    622,
                    671,
                    648,
                    671,
                    648,
                    681,
                    622,
                    681
                  ],
                  "spans": [
                    {
                      "offset": 924,
                      "length": 5
                    }
                  ]
                },
                {
                  "content": "₹ 7,08,000.00",
                  "polygon": [
                    809,
                    670,
                    877,
                    669,
                    877,
                    681,
                    809,
                    681
                  ],
                  "spans": [
                    {
                      "offset": 930,
                      "length": 13
                    }
                  ]
                },
                {
                  "content": "Khar West, Mumbai, Maharashtra 400052",
                  "polygon": [
                    304,
                    692,
                    494,
                    692,
                    494,
                    704,
                    304,
                    704
                  ],
                  "spans": [
                    {
                      "offset": 944,
                      "length": 37
                    }
                  ]
                },
                {
                  "content": "Advance",
                  "polygon": [
                    622,
                    689,
                    665,
                    689,
                    665,
                    700,
                    622,
                    699
                  ],
                  "spans": [
                    {
                      "offset": 982,
                      "length": 7
                    }
                  ]
                },
                {
                  "content": "₹ 0.00",
                  "polygon": [
                    846,
                    688,
                    878,
                    688,
                    878,
                    699,
                    846,
                    699
                  ],
                  "spans": [
                    {
                      "offset": 990,
                      "length": 6
                    }
                  ]
                },
                {
                  "content": "India",
                  "polygon": [
                    305,
                    712,
                    328,
                    712,
                    328,
                    722,
                    305,
                    722
                  ],
                  "spans": [
                    {
                      "offset": 997,
                      "length": 5
                    }
                  ]
                },
                {
                  "content": "TOTAL DUE",
                  "polygon": [
                    623,
                    710,
                    714,
                    710,
                    714,
                    726,
                    623,
                    726
                  ],
                  "spans": [
                    {
                      "offset": 1003,
                      "length": 9
                    }
                  ]
                },
                {
                  "content": "₹ 7,08,000.00",
                  "polygon": [
                    790,
                    709,
                    876,
                    709,
                    876,
                    722,
                    790,
                    722
                  ],
                  "spans": [
                    {
                      "offset": 1013,
                      "length": 13
                    }
                  ]
                },
                {
                  "content": "THANK YOU.",
                  "polygon": [
                    789,
                    739,
                    877,
                    739,
                    877,
                    755,
                    789,
                    755
                  ],
                  "spans": [
                    {
                      "offset": 1027,
                      "length": 10
                    }
                  ]
                }
              ],
              "spans": [
                {
                  "offset": 0,
                  "length": 1037
                }
              ]
            }
          ],
          "tables": [
            {
              "rowCount": 2,
              "columnCount": 3,
              "cells": [
                {
                  "kind": "columnHeader",
                  "rowIndex": 0,
                  "columnIndex": 0,
                  "content": "DATE",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        565,
                        179,
                        664,
                        180,
                        664,
                        219,
                        565,
                        219
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 259,
                      "length": 4
                    }
                  ]
                },
                {
                  "kind": "columnHeader",
                  "rowIndex": 0,
                  "columnIndex": 1,
                  "content": "PLEASE PAY",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        664,
                        180,
                        774,
                        179,
                        774,
                        219,
                        664,
                        219
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 264,
                      "length": 10
                    }
                  ]
                },
                {
                  "kind": "columnHeader",
                  "rowIndex": 0,
                  "columnIndex": 2,
                  "content": "DUE DATE",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        774,
                        179,
                        872,
                        180,
                        872,
                        219,
                        774,
                        219
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 275,
                      "length": 8
                    }
                  ]
                },
                {
                  "rowIndex": 1,
                  "columnIndex": 0,
                  "content": "31-12-2022",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        565,
                        219,
                        664,
                        219,
                        664,
                        247,
                        565,
                        247
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 335,
                      "length": 10
                    }
                  ]
                },
                {
                  "rowIndex": 1,
                  "columnIndex": 1,
                  "content": "₹ 6,54,321.00",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        664,
                        219,
                        774,
                        219,
                        774,
                        247,
                        664,
                        247
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 346,
                      "length": 13
                    }
                  ]
                },
                {
                  "rowIndex": 1,
                  "columnIndex": 2,
                  "content": "31-03-2023",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        774,
                        219,
                        872,
                        219,
                        872,
                        248,
                        774,
                        247
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 360,
                      "length": 10
                    }
                  ]
                }
              ],
              "boundingRegions": [
                {
                  "pageNumber": 1,
                  "polygon": [
                    556,
                    182,
                    879,
                    182,
                    879,
                    253,
                    556,
                    253
                  ]
                }
              ],
              "spans": [
                {
                  "offset": 259,
                  "length": 24
                },
                {
                  "offset": 335,
                  "length": 35
                }
              ]
            },
            {
              "rowCount": 3,
              "columnCount": 2,
              "cells": [
                {
                  "rowIndex": 0,
                  "columnIndex": 0,
                  "content": "State Code:",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        308,
                        286,
                        432,
                        287,
                        432,
                        311,
                        307,
                        311
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 398,
                      "length": 11
                    }
                  ]
                },
                {
                  "rowIndex": 0,
                  "columnIndex": 1,
                  "content": "5",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        432,
                        287,
                        564,
                        288,
                        564,
                        312,
                        432,
                        311
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 410,
                      "length": 1
                    }
                  ]
                },
                {
                  "rowIndex": 1,
                  "columnIndex": 0,
                  "content": "GSTIN:",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        307,
                        311,
                        432,
                        311,
                        432,
                        330,
                        307,
                        329
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 412,
                      "length": 6
                    }
                  ]
                },
                {
                  "rowIndex": 1,
                  "columnIndex": 1,
                  "content": "98AAAAA7654Z3Z2",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        432,
                        311,
                        564,
                        312,
                        564,
                        331,
                        432,
                        330
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 419,
                      "length": 15
                    }
                  ]
                },
                {
                  "rowIndex": 2,
                  "columnIndex": 0,
                  "content": "PLACE OF SUPPLY:",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        307,
                        329,
                        432,
                        330,
                        431,
                        371,
                        306,
                        371
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 435,
                      "length": 16
                    }
                  ]
                },
                {
                  "rowIndex": 2,
                  "columnIndex": 1,
                  "content": "5\nMaharashtra",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        432,
                        330,
                        564,
                        331,
                        564,
                        371,
                        431,
                        371
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 452,
                      "length": 13
                    }
                  ]
                }
              ],
              "boundingRegions": [
                {
                  "pageNumber": 1,
                  "polygon": [
                    317,
                    293,
                    559,
                    293,
                    559,
                    349,
                    317,
                    349
                  ]
                }
              ],
              "spans": [
                {
                  "offset": 398,
                  "length": 67
                }
              ]
            },
            {
              "rowCount": 3,
              "columnCount": 7,
              "cells": [
                {
                  "kind": "columnHeader",
                  "rowIndex": 0,
                  "columnIndex": 0,
                  "content": "S.NO",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        304,
                        370,
                        361,
                        370,
                        361,
                        407,
                        304,
                        407
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 466,
                      "length": 4
                    }
                  ]
                },
                {
                  "kind": "columnHeader",
                  "rowIndex": 0,
                  "columnIndex": 1,
                  "content": "DESCRIPTION",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        361,
                        370,
                        601,
                        370,
                        600,
                        407,
                        361,
                        407
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 471,
                      "length": 11
                    }
                  ]
                },
                {
                  "kind": "columnHeader",
                  "rowIndex": 0,
                  "columnIndex": 2,
                  "content": "HSN/SAC",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        601,
                        370,
                        678,
                        370,
                        678,
                        407,
                        600,
                        407
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 483,
                      "length": 7
                    }
                  ]
                },
                {
                  "kind": "columnHeader",
                  "rowIndex": 0,
                  "columnIndex": 3,
                  "content": "IGST",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        678,
                        370,
                        719,
                        370,
                        719,
                        407,
                        678,
                        407
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 491,
                      "length": 4
                    }
                  ]
                },
                {
                  "kind": "columnHeader",
                  "rowIndex": 0,
                  "columnIndex": 4,
                  "content": "SGST",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        719,
                        370,
                        762,
                        370,
                        762,
                        407,
                        719,
                        407
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 496,
                      "length": 4
                    }
                  ]
                },
                {
                  "kind": "columnHeader",
                  "rowIndex": 0,
                  "columnIndex": 5,
                  "content": "CGST",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        762,
                        370,
                        805,
                        370,
                        805,
                        407,
                        762,
                        407
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 501,
                      "length": 4
                    }
                  ]
                },
                {
                  "kind": "columnHeader",
                  "rowIndex": 0,
                  "columnIndex": 6,
                  "content": "AMOUNT",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        805,
                        370,
                        886,
                        370,
                        886,
                        407,
                        805,
                        407
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 506,
                      "length": 6
                    }
                  ]
                },
                {
                  "rowIndex": 1,
                  "columnIndex": 0,
                  "content": "1",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        304,
                        407,
                        361,
                        407,
                        361,
                        449,
                        304,
                        449
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 556,
                      "length": 1
                    }
                  ]
                },
                {
                  "rowIndex": 1,
                  "columnIndex": 1,
                  "content": "PO# 99112233: IGNITE 2023 Posters, banners\nand wristbands designs",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        361,
                        407,
                        600,
                        407,
                        600,
                        449,
                        361,
                        449
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 513,
                      "length": 42
                    },
                    {
                      "offset": 558,
                      "length": 22
                    }
                  ]
                },
                {
                  "rowIndex": 1,
                  "columnIndex": 2,
                  "content": "998877",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        600,
                        407,
                        678,
                        407,
                        678,
                        449,
                        600,
                        449
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 581,
                      "length": 6
                    }
                  ]
                },
                {
                  "rowIndex": 1,
                  "columnIndex": 3,
                  "content": "18%",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        678,
                        407,
                        719,
                        407,
                        719,
                        449,
                        678,
                        449
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 588,
                      "length": 3
                    }
                  ]
                },
                {
                  "rowIndex": 1,
                  "columnIndex": 4,
                  "content": "0%",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        719,
                        407,
                        762,
                        407,
                        762,
                        449,
                        719,
                        449
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 592,
                      "length": 2
                    }
                  ]
                },
                {
                  "rowIndex": 1,
                  "columnIndex": 5,
                  "content": "0%",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        762,
                        407,
                        805,
                        407,
                        805,
                        449,
                        762,
                        449
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 595,
                      "length": 2
                    }
                  ]
                },
                {
                  "rowIndex": 1,
                  "columnIndex": 6,
                  "content": "₹ 4,50,000.00",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        805,
                        407,
                        886,
                        407,
                        887,
                        449,
                        805,
                        449
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 598,
                      "length": 13
                    }
                  ]
                },
                {
                  "rowIndex": 2,
                  "columnIndex": 0,
                  "content": "1",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        304,
                        449,
                        361,
                        449,
                        361,
                        490,
                        304,
                        490
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 653,
                      "length": 1
                    }
                  ]
                },
                {
                  "rowIndex": 2,
                  "columnIndex": 1,
                  "content": "PO# 99112233: INSPIRE 2023 Advertisement\ncampaign consulting service",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        361,
                        449,
                        600,
                        449,
                        600,
                        490,
                        361,
                        490
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 612,
                      "length": 40
                    },
                    {
                      "offset": 686,
                      "length": 27
                    }
                  ]
                },
                {
                  "rowIndex": 2,
                  "columnIndex": 2,
                  "content": "112233",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        600,
                        449,
                        678,
                        449,
                        678,
                        490,
                        600,
                        490
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 655,
                      "length": 6
                    }
                  ]
                },
                {
                  "rowIndex": 2,
                  "columnIndex": 3,
                  "content": "18%",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        678,
                        449,
                        719,
                        449,
                        719,
                        490,
                        678,
                        490
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 662,
                      "length": 3
                    }
                  ]
                },
                {
                  "rowIndex": 2,
                  "columnIndex": 4,
                  "content": "0%",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        719,
                        449,
                        762,
                        449,
                        762,
                        490,
                        719,
                        490
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 666,
                      "length": 2
                    }
                  ]
                },
                {
                  "rowIndex": 2,
                  "columnIndex": 5,
                  "content": "0%",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        762,
                        449,
                        805,
                        449,
                        805,
                        490,
                        762,
                        490
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 669,
                      "length": 2
                    }
                  ]
                },
                {
                  "rowIndex": 2,
                  "columnIndex": 6,
                  "content": "₹ 1,50,000.00",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        805,
                        449,
                        887,
                        449,
                        887,
                        490,
                        805,
                        490
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 672,
                      "length": 13
                    }
                  ]
                }
              ],
              "boundingRegions": [
                {
                  "pageNumber": 1,
                  "polygon": [
                    304,
                    375,
                    881,
                    374,
                    881,
                    479,
                    305,
                    479
                  ]
                }
              ],
              "spans": [
                {
                  "offset": 466,
                  "length": 46
                },
                {
                  "offset": 556,
                  "length": 1
                },
                {
                  "offset": 513,
                  "length": 42
                },
                {
                  "offset": 558,
                  "length": 53
                },
                {
                  "offset": 653,
                  "length": 1
                },
                {
                  "offset": 612,
                  "length": 40
                },
                {
                  "offset": 686,
                  "length": 27
                },
                {
                  "offset": 655,
                  "length": 30
                }
              ]
            },
            {
              "rowCount": 7,
              "columnCount": 2,
              "cells": [
                {
                  "rowIndex": 0,
                  "columnIndex": 0,
                  "content": "SUBTOTAL",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        610,
                        589,
                        750,
                        589,
                        750,
                        608,
                        610,
                        608
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 740,
                      "length": 8
                    }
                  ]
                },
                {
                  "rowIndex": 0,
                  "columnIndex": 1,
                  "content": "₹ 6,00,000.00",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        750,
                        589,
                        885,
                        589,
                        885,
                        608,
                        750,
                        608
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 749,
                      "length": 13
                    }
                  ]
                },
                {
                  "rowIndex": 1,
                  "columnIndex": 0,
                  "content": "IGST",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        610,
                        608,
                        750,
                        608,
                        750,
                        627,
                        610,
                        627
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 784,
                      "length": 4
                    }
                  ]
                },
                {
                  "rowIndex": 1,
                  "columnIndex": 1,
                  "content": "₹ 1,08,000.00",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        750,
                        608,
                        885,
                        608,
                        885,
                        627,
                        750,
                        627
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 789,
                      "length": 13
                    }
                  ]
                },
                {
                  "rowIndex": 2,
                  "columnIndex": 0,
                  "content": "SGST",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        610,
                        627,
                        750,
                        627,
                        750,
                        646,
                        610,
                        647
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 826,
                      "length": 4
                    }
                  ]
                },
                {
                  "rowIndex": 2,
                  "columnIndex": 1,
                  "content": "₹ 0.00",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        750,
                        627,
                        885,
                        627,
                        885,
                        646,
                        750,
                        646
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 831,
                      "length": 6
                    }
                  ]
                },
                {
                  "rowIndex": 3,
                  "columnIndex": 0,
                  "content": "CGST",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        610,
                        647,
                        750,
                        646,
                        750,
                        665,
                        610,
                        665
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 870,
                      "length": 4
                    }
                  ]
                },
                {
                  "rowIndex": 3,
                  "columnIndex": 1,
                  "content": "₹ 0.00",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        750,
                        646,
                        885,
                        646,
                        885,
                        665,
                        750,
                        665
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 875,
                      "length": 6
                    }
                  ]
                },
                {
                  "rowIndex": 4,
                  "columnIndex": 0,
                  "content": "Total",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        610,
                        665,
                        750,
                        665,
                        750,
                        685,
                        610,
                        685
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 924,
                      "length": 5
                    }
                  ]
                },
                {
                  "rowIndex": 4,
                  "columnIndex": 1,
                  "content": "₹ 7,08,000.00",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        750,
                        665,
                        885,
                        665,
                        885,
                        685,
                        750,
                        685
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 930,
                      "length": 13
                    }
                  ]
                },
                {
                  "rowIndex": 5,
                  "columnIndex": 0,
                  "content": "Advance",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        610,
                        685,
                        750,
                        685,
                        750,
                        702,
                        610,
                        702
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 982,
                      "length": 7
                    }
                  ]
                },
                {
                  "rowIndex": 5,
                  "columnIndex": 1,
                  "content": "₹ 0.00",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        750,
                        685,
                        885,
                        685,
                        885,
                        702,
                        750,
                        702
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 990,
                      "length": 6
                    }
                  ]
                },
                {
                  "rowIndex": 6,
                  "columnIndex": 0,
                  "content": "TOTAL DUE",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        610,
                        702,
                        750,
                        702,
                        750,
                        734,
                        610,
                        733
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 1003,
                      "length": 9
                    }
                  ]
                },
                {
                  "rowIndex": 6,
                  "columnIndex": 1,
                  "content": "₹ 7,08,000.00",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        750,
                        702,
                        885,
                        702,
                        885,
                        734,
                        750,
                        734
                      ]
                    }
                  ],
                  "spans": [
                    {
                      "offset": 1013,
                      "length": 13
                    }
                  ]
                }
              ],
              "boundingRegions": [
                {
                  "pageNumber": 1,
                  "polygon": [
                    616,
                    591,
                    880,
                    591,
                    880,
                    732,
                    616,
                    732
                  ]
                }
              ],
              "spans": [
                {
                  "offset": 740,
                  "length": 22
                },
                {
                  "offset": 784,
                  "length": 18
                },
                {
                  "offset": 826,
                  "length": 11
                },
                {
                  "offset": 870,
                  "length": 11
                },
                {
                  "offset": 924,
                  "length": 19
                },
                {
                  "offset": 982,
                  "length": 14
                },
                {
                  "offset": 1003,
                  "length": 23
                }
              ]
            }
          ],
          "styles": [],
          "documents": [
            {
              "docType": "invoice",
              "boundingRegions": [
                {
                  "pageNumber": 1,
                  "polygon": [
                    0,
                    0,
                    1200,
                    0,
                    1200,
                    893,
                    0,
                    893
                  ]
                }
              ],
              "fields": {
                "AmountDue": {
                  "type": "currency",
                  "valueCurrency": {
                    "currencySymbol": "₹",
                    "amount": 708000,
                    "currencyCode": "INR"
                  },
                  "content": "₹ 7,08,000.00",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        790,
                        709,
                        877,
                        709,
                        877,
                        722,
                        790,
                        722
                      ]
                    }
                  ],
                  "confidence": 0.816,
                  "spans": [
                    {
                      "offset": 1013,
                      "length": 13
                    }
                  ]
                },
                "CustomerAddress": {
                  "type": "address",
                  "content": "Level 10, Tower C, DLF Epitome Building No. 5, DLF\nCyber City, Gurgaon 122002",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        304,
                        224,
                        552,
                        224,
                        552,
                        257,
                        304,
                        257
                      ]
                    }
                  ],
                  "confidence": 0.364,
                  "spans": [
                    {
                      "offset": 284,
                      "length": 50
                    },
                    {
                      "offset": 371,
                      "length": 26
                    }
                  ],
                  "valueAddress": {
                    "road": "DLF",
                    "postalCode": "122002",
                    "city": "Gurgaon",
                    "streetAddress": "DLF",
                    "cityDistrict": "Cyber City",
                    "house": "Level 10, Tower C, DLF Epitome Building No. 5"
                  }
                },
                "CustomerAddressRecipient": {
                  "type": "string",
                  "valueString": "Microsoft Corporation India Pvt Ltd",
                  "content": "Microsoft Corporation India Pvt Ltd",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        304,
                        204,
                        477,
                        204,
                        477,
                        216,
                        304,
                        216
                      ]
                    }
                  ],
                  "confidence": 0.417,
                  "spans": [
                    {
                      "offset": 223,
                      "length": 35
                    }
                  ]
                },
                "CustomerName": {
                  "type": "string",
                  "valueString": "Microsoft Corporation India Pvt Ltd",
                  "content": "Microsoft Corporation India Pvt Ltd",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        304,
                        204,
                        477,
                        204,
                        477,
                        216,
                        304,
                        216
                      ]
                    }
                  ],
                  "confidence": 0.417,
                  "spans": [
                    {
                      "offset": 223,
                      "length": 35
                    }
                  ]
                },
                "CustomerTaxId": {
                  "type": "string",
                  "valueString": "98AAAAA7654Z3Z2",
                  "content": "98AAAAA7654Z3Z2",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        457,
                        315,
                        553,
                        315,
                        553,
                        325,
                        457,
                        325
                      ]
                    }
                  ],
                  "confidence": 0.955,
                  "spans": [
                    {
                      "offset": 419,
                      "length": 15
                    }
                  ]
                },
                "DueDate": {
                  "type": "date",
                  "valueDate": "2023-03-31",
                  "content": "31-03-2023",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        793,
                        225,
                        855,
                        225,
                        855,
                        236,
                        793,
                        236
                      ]
                    }
                  ],
                  "confidence": 0.959,
                  "spans": [
                    {
                      "offset": 360,
                      "length": 10
                    }
                  ]
                },
                "InvoiceDate": {
                  "type": "date",
                  "valueDate": "2022-12-31",
                  "content": "31-12-2022",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        585,
                        225,
                        646,
                        225,
                        646,
                        236,
                        585,
                        236
                      ]
                    }
                  ],
                  "confidence": 0.959,
                  "spans": [
                    {
                      "offset": 335,
                      "length": 10
                    }
                  ]
                },
                "InvoiceId": {
                  "type": "string",
                  "valueString": "MSFT0011223344",
                  "content": "MSFT0011223344",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        532,
                        146,
                        678,
                        146,
                        678,
                        162,
                        532,
                        162
                      ]
                    }
                  ],
                  "confidence": 0.95,
                  "spans": [
                    {
                      "offset": 182,
                      "length": 14
                    }
                  ]
                },
                "InvoiceTotal": {
                  "type": "currency",
                  "valueCurrency": {
                    "currencySymbol": "₹",
                    "amount": 708000,
                    "currencyCode": "INR"
                  },
                  "content": "₹ 7,08,000.00",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        809,
                        669,
                        878,
                        669,
                        878,
                        681,
                        809,
                        681
                      ]
                    }
                  ],
                  "confidence": 0.895,
                  "spans": [
                    {
                      "offset": 930,
                      "length": 13
                    }
                  ]
                },
                "Items": {
                  "type": "array",
                  "valueArray": [
                    {
                      "type": "object",
                      "valueObject": {
                        "Amount": {
                          "type": "currency",
                          "valueCurrency": {
                            "currencySymbol": "₹",
                            "amount": 450000,
                            "currencyCode": "INR"
                          },
                          "content": "₹ 4,50,000.00",
                          "boundingRegions": [
                            {
                              "pageNumber": 1,
                              "polygon": [
                                815,
                                424,
                                879,
                                424,
                                879,
                                436,
                                815,
                                436
                              ]
                            }
                          ],
                          "confidence": 0.938,
                          "spans": [
                            {
                              "offset": 598,
                              "length": 13
                            }
                          ]
                        },
                        "Description": {
                          "type": "string",
                          "valueString": "PO# 99112233: IGNITE 2023 Posters, banners\nand wristbands designs",
                          "content": "PO# 99112233: IGNITE 2023 Posters, banners\nand wristbands designs",
                          "boundingRegions": [
                            {
                              "pageNumber": 1,
                              "polygon": [
                                377,
                                416,
                                578,
                                416,
                                578,
                                445,
                                377,
                                445
                              ]
                            }
                          ],
                          "confidence": 0.937,
                          "spans": [
                            {
                              "offset": 513,
                              "length": 42
                            },
                            {
                              "offset": 558,
                              "length": 22
                            }
                          ]
                        },
                        "ProductCode": {
                          "type": "string",
                          "valueString": "998877",
                          "content": "998877",
                          "boundingRegions": [
                            {
                              "pageNumber": 1,
                              "polygon": [
                                629,
                                424,
                                665,
                                424,
                                665,
                                435,
                                629,
                                435
                              ]
                            }
                          ],
                          "confidence": 0.629,
                          "spans": [
                            {
                              "offset": 581,
                              "length": 6
                            }
                          ]
                        },
                        "TaxRate": {
                          "type": "string",
                          "valueString": "18%\n0%\n0%",
                          "content": "18%\n0%\n0%",
                          "boundingRegions": [
                            {
                              "pageNumber": 1,
                              "polygon": [
                                688,
                                424,
                                793,
                                424,
                                793,
                                435,
                                688,
                                435
                              ]
                            }
                          ],
                          "confidence": 0.938,
                          "spans": [
                            {
                              "offset": 588,
                              "length": 9
                            }
                          ]
                        }
                      },
                      "content": "PO# 99112233: IGNITE 2023 Posters, banners\n1\nand wristbands designs\n998877\n18%\n0%\n0%\n₹ 4,50,000.00",
                      "boundingRegions": [
                        {
                          "pageNumber": 1,
                          "polygon": [
                            331,
                            416,
                            879,
                            416,
                            879,
                            445,
                            331,
                            445
                          ]
                        }
                      ],
                      "confidence": 0.922,
                      "spans": [
                        {
                          "offset": 513,
                          "length": 98
                        }
                      ]
                    },
                    {
                      "type": "object",
                      "valueObject": {
                        "Amount": {
                          "type": "currency",
                          "valueCurrency": {
                            "currencySymbol": "₹",
                            "amount": 150000,
                            "currencyCode": "INR"
                          },
                          "content": "₹ 1,50,000.00",
                          "boundingRegions": [
                            {
                              "pageNumber": 1,
                              "polygon": [
                                815,
                                461,
                                879,
                                461,
                                879,
                                473,
                                815,
                                473
                              ]
                            }
                          ],
                          "confidence": 0.939,
                          "spans": [
                            {
                              "offset": 672,
                              "length": 13
                            }
                          ]
                        },
                        "Description": {
                          "type": "string",
                          "valueString": "PO# 99112233: INSPIRE 2023 Advertisement\ncampaign consulting service",
                          "content": "PO# 99112233: INSPIRE 2023 Advertisement\ncampaign consulting service",
                          "boundingRegions": [
                            {
                              "pageNumber": 1,
                              "polygon": [
                                376,
                                455,
                                574,
                                455,
                                574,
                                485,
                                376,
                                485
                              ]
                            }
                          ],
                          "confidence": 0.938,
                          "spans": [
                            {
                              "offset": 612,
                              "length": 40
                            },
                            {
                              "offset": 686,
                              "length": 27
                            }
                          ]
                        },
                        "ProductCode": {
                          "type": "string",
                          "valueString": "112233",
                          "content": "112233",
                          "boundingRegions": [
                            {
                              "pageNumber": 1,
                              "polygon": [
                                630,
                                462,
                                665,
                                461,
                                665,
                                472,
                                630,
                                472
                              ]
                            }
                          ],
                          "confidence": 0.716,
                          "spans": [
                            {
                              "offset": 655,
                              "length": 6
                            }
                          ]
                        },
                        "TaxRate": {
                          "type": "string",
                          "valueString": "18%\n0%\n0%",
                          "content": "18%\n0%\n0%",
                          "boundingRegions": [
                            {
                              "pageNumber": 1,
                              "polygon": [
                                688,
                                462,
                                794,
                                462,
                                794,
                                472,
                                688,
                                472
                              ]
                            }
                          ],
                          "confidence": 0.939,
                          "spans": [
                            {
                              "offset": 662,
                              "length": 9
                            }
                          ]
                        }
                      },
                      "content": "PO# 99112233: INSPIRE 2023 Advertisement\n1\n112233\n18%\n0%\n0%\n₹ 1,50,000.00\ncampaign consulting service",
                      "boundingRegions": [
                        {
                          "pageNumber": 1,
                          "polygon": [
                            331,
                            455,
                            879,
                            455,
                            879,
                            485,
                            331,
                            485
                          ]
                        }
                      ],
                      "confidence": 0.921,
                      "spans": [
                        {
                          "offset": 612,
                          "length": 101
                        }
                      ]
                    }
                  ]
                },
                "PaymentDetails": {
                  "type": "array",
                  "valueArray": [
                    {
                      "type": "object",
                      "valueObject": {
                        "SWIFT": {
                          "type": "string",
                          "valueString": "MSFTINB123",
                          "content": "MSFTINB123",
                          "boundingRegions": [
                            {
                              "pageNumber": 1,
                              "polygon": [
                                364,
                                633,
                                428,
                                633,
                                428,
                                645,
                                364,
                                645
                              ]
                            }
                          ],
                          "confidence": 0.98,
                          "spans": [
                            {
                              "offset": 815,
                              "length": 10
                            }
                          ]
                        }
                      },
                      "confidence": 0.995
                    }
                  ]
                },
                "PurchaseOrder": {
                  "type": "string",
                  "valueString": "99112233:",
                  "content": "99112233:",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        398,
                        455,
                        444,
                        455,
                        444,
                        467,
                        398,
                        466
                      ]
                    }
                  ],
                  "confidence": 0.938,
                  "spans": [
                    {
                      "offset": 616,
                      "length": 9
                    }
                  ]
                },
                "RemittanceAddressRecipient": {
                  "type": "string",
                  "valueString": "Contoso Bank LTD,",
                  "content": "Contoso Bank LTD,",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        352,
                        672,
                        440,
                        672,
                        440,
                        685,
                        352,
                        685
                      ]
                    }
                  ],
                  "confidence": 0.351,
                  "spans": [
                    {
                      "offset": 891,
                      "length": 17
                    }
                  ]
                },
                "SubTotal": {
                  "type": "currency",
                  "valueCurrency": {
                    "currencySymbol": "₹",
                    "amount": 600000,
                    "currencyCode": "INR"
                  },
                  "content": "₹ 6,00,000.00",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        809,
                        595,
                        878,
                        595,
                        878,
                        606,
                        809,
                        606
                      ]
                    }
                  ],
                  "confidence": 0.94,
                  "spans": [
                    {
                      "offset": 749,
                      "length": 13
                    }
                  ]
                },
                "TaxDetails": {
                  "type": "array",
                  "valueArray": [
                    {
                      "type": "object",
                      "valueObject": {
                        "Amount": {
                          "type": "currency",
                          "valueCurrency": {
                            "currencySymbol": "₹",
                            "amount": 108000,
                            "currencyCode": "INR"
                          },
                          "content": "₹ 1,08,000.00",
                          "boundingRegions": [
                            {
                              "pageNumber": 1,
                              "polygon": [
                                809,
                                613,
                                878,
                                613,
                                878,
                                625,
                                809,
                                625
                              ]
                            }
                          ],
                          "confidence": 0.94,
                          "spans": [
                            {
                              "offset": 789,
                              "length": 13
                            }
                          ]
                        }
                      },
                      "content": "IGST\n₹ 1,08,000.00",
                      "boundingRegions": [
                        {
                          "pageNumber": 1,
                          "polygon": [
                            622,
                            613,
                            878,
                            613,
                            878,
                            625,
                            622,
                            625
                          ]
                        }
                      ],
                      "confidence": 0.899,
                      "spans": [
                        {
                          "offset": 784,
                          "length": 18
                        }
                      ]
                    },
                    {
                      "type": "object",
                      "valueObject": {
                        "Amount": {
                          "type": "currency",
                          "valueCurrency": {
                            "currencySymbol": "₹",
                            "amount": 0,
                            "currencyCode": "INR"
                          },
                          "content": "₹ 0.00",
                          "boundingRegions": [
                            {
                              "pageNumber": 1,
                              "polygon": [
                                846,
                                632,
                                877,
                                632,
                                877,
                                643,
                                846,
                                643
                              ]
                            }
                          ],
                          "confidence": 0.939,
                          "spans": [
                            {
                              "offset": 831,
                              "length": 6
                            }
                          ]
                        }
                      },
                      "content": "SGST\n₹ 0.00",
                      "boundingRegions": [
                        {
                          "pageNumber": 1,
                          "polygon": [
                            622,
                            632,
                            877,
                            632,
                            877,
                            643,
                            622,
                            643
                          ]
                        }
                      ],
                      "confidence": 0.898,
                      "spans": [
                        {
                          "offset": 826,
                          "length": 11
                        }
                      ]
                    },
                    {
                      "type": "object",
                      "valueObject": {
                        "Amount": {
                          "type": "currency",
                          "valueCurrency": {
                            "currencySymbol": "₹",
                            "amount": 0,
                            "currencyCode": "INR"
                          },
                          "content": "₹ 0.00",
                          "boundingRegions": [
                            {
                              "pageNumber": 1,
                              "polygon": [
                                846,
                                651,
                                878,
                                651,
                                878,
                                662,
                                846,
                                662
                              ]
                            }
                          ],
                          "confidence": 0.937,
                          "spans": [
                            {
                              "offset": 875,
                              "length": 6
                            }
                          ]
                        }
                      },
                      "content": "CGST\n₹ 0.00",
                      "boundingRegions": [
                        {
                          "pageNumber": 1,
                          "polygon": [
                            622,
                            651,
                            878,
                            651,
                            878,
                            662,
                            622,
                            662
                          ]
                        }
                      ],
                      "confidence": 0.898,
                      "spans": [
                        {
                          "offset": 870,
                          "length": 11
                        }
                      ]
                    }
                  ]
                },
                "TotalTax": {
                  "type": "currency",
                  "valueCurrency": {
                    "currencySymbol": "₹",
                    "amount": 108000,
                    "currencyCode": "INR"
                  },
                  "content": "₹ 1,08,000.00",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        809,
                        613,
                        878,
                        613,
                        878,
                        625,
                        809,
                        625
                      ]
                    }
                  ],
                  "confidence": 0.692,
                  "spans": [
                    {
                      "offset": 789,
                      "length": 13
                    }
                  ]
                },
                "VendorAddress": {
                  "type": "address",
                  "content": "Windsor tower, 123th Floor, Salsette Road\nKalina, Santacruz East, Mumbai, Maharashtra\n400098",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        304,
                        118,
                        503,
                        118,
                        503,
                        164,
                        304,
                        164
                      ]
                    }
                  ],
                  "confidence": 0.645,
                  "spans": [
                    {
                      "offset": 46,
                      "length": 41
                    },
                    {
                      "offset": 108,
                      "length": 50
                    }
                  ],
                  "valueAddress": {
                    "road": "123th Floor, Salsette Road",
                    "postalCode": "400098",
                    "city": "Mumbai",
                    "state": "Maharashtra",
                    "streetAddress": "123th Floor, Salsette Road",
                    "suburb": "Kalina, Santacruz East",
                    "house": "Windsor tower"
                  }
                },
                "VendorAddressRecipient": {
                  "type": "string",
                  "valueString": "Contoso LTD",
                  "content": "Contoso LTD",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        305,
                        100,
                        363,
                        100,
                        363,
                        110,
                        305,
                        110
                      ]
                    }
                  ],
                  "confidence": 0.94,
                  "spans": [
                    {
                      "offset": 34,
                      "length": 11
                    }
                  ]
                },
                "VendorName": {
                  "type": "string",
                  "valueString": "Contoso",
                  "content": "Contoso",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        776,
                        122,
                        871,
                        124,
                        871,
                        150,
                        776,
                        153
                      ]
                    }
                  ],
                  "confidence": 0.956,
                  "spans": [
                    {
                      "offset": 100,
                      "length": 7
                    }
                  ]
                },
                "VendorTaxId": {
                  "type": "string",
                  "valueString": "12ABCDE0123A1A2",
                  "content": "12ABCDE0123A1A2",
                  "boundingRegions": [
                    {
                      "pageNumber": 1,
                      "polygon": [
                        373,
                        154,
                        460,
                        154,
                        460,
                        164,
                        373,
                        164
                      ]
                    }
                  ],
                  "confidence": 0.944,
                  "spans": [
                    {
                      "offset": 166,
                      "length": 15
                    }
                  ]
                }
              },
              "confidence": 1,
              "spans": [
                {
                  "offset": 0,
                  "length": 1037
                }
              ]
            }
          ],
          "contentFormat": "text"
        }
      }
    }
    logger.debug('--- Outgoing response ---')
    logger.debug(json.dumps(resp)[:4096])
    return func.HttpResponse(
        json.dumps(resp),
        status_code=200,
        mimetype="application/json"
    )
