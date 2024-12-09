from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        total = n * (n + 1) // 2
        rs = n
        bset = set(banned)
        for b in bset:
            if b <= n:
                total -= b
                rs -= 1
        cur = n
        while total > maxSum:
            if cur not in bset:
                total -= cur
                rs -= 1
            cur -= 1
        return rs


print(
    Solution().maxCount(
        [
            87,
            193,
            85,
            55,
            14,
            69,
            26,
            133,
            171,
            180,
            4,
            8,
            29,
            121,
            182,
            78,
            157,
            53,
            26,
            7,
            117,
            138,
            57,
            167,
            8,
            103,
            32,
            110,
            15,
            190,
            139,
            16,
            49,
            138,
            68,
            69,
            92,
            89,
            140,
            149,
            107,
            104,
            2,
            135,
            193,
            87,
            21,
            194,
            192,
            9,
            161,
            188,
            73,
            84,
            83,
            31,
            86,
            33,
            138,
            63,
            127,
            73,
            114,
            32,
            66,
            64,
            19,
            175,
            108,
            80,
            176,
            52,
            124,
            94,
            33,
            55,
            130,
            147,
            39,
            76,
            22,
            112,
            113,
            136,
            100,
            134,
            155,
            40,
            170,
            144,
            37,
            43,
            151,
            137,
            82,
            127,
            73,
        ],
        1079,
        87,
    )
)
