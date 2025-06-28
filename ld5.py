import cloudscraper
import time
import os
from colorama import Fore, Style, init
import json
import random
# Khởi tạo colorama
init(autoreset=True)

# Danh sách User-Agent
USER_AGENTS = [
    "Mozilla/5.0 (Linux; Android 11; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.400.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.102.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.30.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.142.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/902.25 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Pixel5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/957.34 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Samsung11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/831.43 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.9829.263 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.7410.646 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.9587.633 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi18) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6694.428 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel17) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.8847.492 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/874.19 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi17) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5001.174 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Samsung3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/815.33 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5019.321 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Samsung3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.8832.313 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Samsung18) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/977.22 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.7748.583 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.9206.396 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Samsung12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/983.43 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/853.30 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi18) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.7111.231 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.8258.647 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; Pixel2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/700.45 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Samsung10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/659.20 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Pixel10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.8576.872 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi17) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/849.15 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Samsung3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/919.18 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Samsung12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/945.35 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Pixel16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/681.21 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/811.43 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/797.10 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Samsung16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/622.14 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Pixel11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5869.160 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6926.809 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Samsung8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.6308.734 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Pixel7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5770.188 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/972.11 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Pixel10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/738.22 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Samsung8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6129.474 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.7810.187 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Samsung5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/825.50 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Samsung14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/715.25 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Samsung19) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/887.29 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.9811.655 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.6539.684 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi18) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.8273.481 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/717.28 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.8511.709 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5124.311 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Samsung4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.8757.173 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Samsung7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/874.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Samsung8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.7494.328 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Pixel11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/970.22 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi17) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/963.37 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Samsung16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/969.6 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Samsung10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/673.30 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/776.32 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/752.49 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi19) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/906.21 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/728.23 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Samsung19) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.7614.643 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Pixel12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.7227.638 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; Pixel8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/844.40 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.6084.946 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Samsung11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.7683.489 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/921.20 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/671.8 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Pixel12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/891.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/652.26 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Pixel14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/917.30 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Samsung9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6044.249 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Samsung2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.6638.543 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Samsung16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/793.42 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.8913.388 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.8241.681 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.5237.423 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel18) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5915.842 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel17) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.9051.968 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.9551.899 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Samsung12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/799.19 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.7799.792 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/841.45 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi17) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5298.936 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi17) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/639.36 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6057.807 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Pixel20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/785.47 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/639.30 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.7178.873 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/842.4 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Samsung19) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/937.43 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Samsung20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.7112.922 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.6672.223 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.7117.907 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi18) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6834.985 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/856.17 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Samsung5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.7830.686 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Samsung1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/741.10 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi17) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.7286.446 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel19) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/760.37 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.7426.739 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Samsung4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6874.865 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/998.38 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Samsung19) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.5425.166 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Samsung1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/771.1 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; Pixel11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/893.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.8237.231 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.6487.792 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Pixel3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/904.4 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Pixel4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/602.34 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Pixel11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5005.427 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Pixel6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.5586.807 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/626.4 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Samsung2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.9778.512 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/727.36 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Pixel12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.7318.996 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Samsung17) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/867.35 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel18) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5471.232 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.8131.381 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/724.19 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; Pixel16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.9710.307 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Samsung18) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/951.23 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Samsung3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/967.21 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/677.23 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Pixel18) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/612.30 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/922.12 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.7008.660 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Samsung1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/998.2 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/925.43 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/967.45 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Samsung9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.9880.876 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.5974.593 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Samsung20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/612.48 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Samsung15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.7564.497 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Samsung13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/811.25 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/845.45 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Samsung6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.7532.763 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.5907.536 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/806.35 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/887.30 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Samsung7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.8165.834 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.9252.196 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Samsung20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/997.21 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.9771.619 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Samsung4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/829.2 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/904.43 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Pixel20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.9538.336 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; Pixel8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/829.21 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/847.38 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/875.48 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/670.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/789.36 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; Pixel6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/875.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/852.47 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5438.383 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Samsung20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6709.300 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.6489.495 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Samsung10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/810.24 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.7538.345 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/872.30 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Samsung7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.5104.328 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/696.29 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi17) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/788.48 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/602.1 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Samsung1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/927.50 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/761.49 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Samsung3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.6654.839 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Samsung2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/972.28 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Pixel14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.8785.573 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Pixel18) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.8948.813 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/681.3 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.7980.497 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Samsung5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/714.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.5474.858 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/942.37 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Samsung5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/752.34 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Pixel13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.6599.254 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Samsung12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/881.37 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Samsung12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.9541.881 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Samsung17) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/664.28 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Samsung3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.9323.828 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5463.347 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Pixel16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/868.28 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Samsung14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/709.16 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Samsung2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/981.20 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; Pixel7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5873.497 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi17) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.8966.647 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/765.37 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Samsung6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.7268.891 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.6891.275 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Samsung20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/697.5 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/893.39 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Samsung16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6274.293 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5645.280 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/652.44 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Samsung5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/702.17 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Samsung5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/720.4 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel18) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/857.32 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Samsung8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/760.13 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel19) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/886.17 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi18) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.5292.445 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/763.38 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Samsung8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/663.34 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel19) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/851.34 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/898.21 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Samsung2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.8090.669 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Samsung5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.8045.244 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Samsung5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.6197.978 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi17) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/786.21 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Pixel3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6395.947 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.9494.112 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Samsung10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/643.19 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.7721.856 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Samsung4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/884.36 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Samsung1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.6223.268 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi17) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/975.35 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Pixel18) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.8681.696 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Samsung16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/933.1 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.8119.856 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Pixel4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/761.31 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Pixel6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.5408.109 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5352.970 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Pixel8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/812.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/899.41 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Samsung18) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/792.17 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5366.732 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Samsung20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/658.44 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5581.462 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Samsung1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/993.6 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Samsung2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/679.39 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/769.16 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.9589.899 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.9342.166 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/738.17 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Pixel3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/702.13 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi17) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/966.36 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.8384.533 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi17) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/893.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/750.38 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Pixel10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.8950.120 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Samsung3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/924.25 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel18) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/719.25 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/942.16 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.8817.241 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Samsung19) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/891.41 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5099.342 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; Pixel5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/788.39 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/897.28 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.6332.547 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.6357.230 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/738.4 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/857.14 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.8574.352 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Samsung14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/844.19 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Samsung8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.6690.378 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Pixel13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.8801.262 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/820.26 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel19) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.7407.228 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Pixel15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.8726.501 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Pixel9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.8250.816 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Samsung18) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/942.13 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Pixel10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/753.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Samsung17) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/990.49 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.8623.346 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6590.690 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Pixel12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.6766.613 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Samsung10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/898.12 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; Pixel2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.6049.680 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Samsung8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/719.27 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/944.1 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Samsung6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.6481.731 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Samsung14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6409.913 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Samsung20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.8367.320 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/911.36 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Samsung12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.5183.358 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel19) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5369.272 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.6772.633 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; Pixel14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/671.28 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Samsung12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5721.527 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; Pixel18) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/804.41 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Samsung8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.9229.750 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/947.19 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/696.5 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Samsung12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/923.29 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Pixel4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.8128.153 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/754.2 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; Pixel20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/613.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Samsung18) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/717.2 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/693.4 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Samsung7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/749.16 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Samsung18) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/907.37 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi18) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.7177.396 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPad OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU iPad OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Pixel18) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.8460.284 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.3.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.230.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.41.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.39.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.291.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.333.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.104.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.237.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.214.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.383.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.313.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.191.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.1.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.41.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.490.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.288.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.19.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.200.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.40.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.113.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.173.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.359.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.365.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.106.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.481.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.201.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.232.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.427.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.484.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.277.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.82.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.221.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.132.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.269.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.445.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.202.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.90.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.168.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.86.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.35.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.83.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.307.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.178.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.428.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.210.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.15.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.338.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.54.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.339.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.233.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.46.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.182.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.299.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.145.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.297.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.17.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.225.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.16.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.16.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.214.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.27.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.81.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.227.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.57.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.100.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.272.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.171.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.221.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.207.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.74.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.135.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.7.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.272.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.313.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.412.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.435.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.342.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.236.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.426.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.233.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.29.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.47.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.281.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.143.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.194.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.85.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.304.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.348.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.137.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.436.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.211.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.354.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.430.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.103.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.296.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.199.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.214.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.2.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.142.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.333.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.423.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.388.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.195.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.231.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.130.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.391.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.272.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.186.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.110.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.370.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.323.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.5.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.340.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.301.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.202.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.398.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.40.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.212.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.32.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.201.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.35.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.306.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.113.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.27.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.488.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.179.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.182.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.124.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.18.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.395.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.211.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.305.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.456.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.123.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.188.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.213.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.196.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.409.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.154.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.485.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.283.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.426.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.183.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.103.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.158.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.110.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.449.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.489.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.20.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.476.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.43.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.148.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.459.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.236.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.109.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.40.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.372.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.165.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.151.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.420.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.490.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.251.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.349.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.213.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.239.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.360.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.146.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.98.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.450.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.237.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.211.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.190.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.481.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.432.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.217.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.368.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.375.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.487.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.405.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.264.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.460.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.141.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.303.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.404.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.289.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.403.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.391.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.442.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.262.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.13.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.327.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.462.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.211.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.67.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.137.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.50.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.86.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.197.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.72.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.379.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.278.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.212.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.165.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.321.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.300.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.124.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.197.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.135.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.17.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.403.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.187.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.57.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.173.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.297.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.348.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.327.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.411.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.345.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.41.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.246.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.439.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.350.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.4.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.438.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.269.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.420.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.267.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.496.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.248.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.46.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.384.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.165.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.85.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.342.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.198.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.387.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.344.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.106.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.311.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.161.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.331.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.418.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.212.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.472.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; OnePlus 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.326.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/117.0.303.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.295.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.4.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.318.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.23.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/119.0.0.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/116.0.453.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/121.0.488.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.212.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.172.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.207.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/121.0.204.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/116.0.280.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.163.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/117.0.467.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/118.0.394.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/119.0.442.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/125.0.371.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.335.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.135.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/118.0.215.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/117.0.287.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/121.0.37.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.45.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/119.0.22.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/118.0.140.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.158.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/113.0.76.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/119.0.110.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/113.0.176.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/118.0.320.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/111.0.196.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.253.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.486.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.106.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.148.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/125.0.316.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/111.0.151.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.202.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.102.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/119.0.370.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/113.0.379.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.415.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/110.0.104.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/125.0.172.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.295.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.348.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/119.0.135.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/121.0.332.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.53.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.66.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.181.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.470.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/112.0.152.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.211.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/111.0.256.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.151.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.311.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.61.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/111.0.80.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/121.0.98.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.48.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/111.0.124.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/113.0.160.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.221.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/117.0.213.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.396.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.488.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/119.0.289.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.241.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/116.0.332.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/113.0.267.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/117.0.190.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/116.0.411.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.483.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/119.0.349.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.52.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/113.0.179.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.387.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/117.0.127.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/112.0.311.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/111.0.354.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.240.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.63.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.455.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/121.0.391.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/116.0.486.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.457.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.430.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.347.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/111.0.22.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/117.0.308.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/113.0.176.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.484.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.164.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/110.0.142.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/116.0.394.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.376.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/112.0.346.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/112.0.484.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.410.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.397.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/110.0.429.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.64.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/112.0.305.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/125.0.405.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.218.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/121.0.9.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.243.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/112.0.342.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/112.0.158.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/110.0.309.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/121.0.196.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/118.0.40.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.353.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/125.0.67.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/117.0.227.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/119.0.46.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.489.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.87.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/117.0.122.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/125.0.305.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/113.0.473.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.60.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.213.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/112.0.88.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.248.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/116.0.400.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/125.0.447.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/116.0.59.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.95.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.312.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/121.0.382.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.44.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.153.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/125.0.335.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.43.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/117.0.488.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.230.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.21.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/118.0.309.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/113.0.236.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.52.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/110.0.399.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/117.0.272.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/125.0.321.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.208.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/116.0.77.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/116.0.148.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.2.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/117.0.456.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.309.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/116.0.310.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/113.0.222.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/117.0.289.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/112.0.295.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/116.0.81.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.306.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/116.0.399.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.237.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.24.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/112.0.277.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.203.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.231.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/116.0.180.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.371.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.113.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/111.0.122.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.266.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/118.0.442.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/116.0.481.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/113.0.7.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/125.0.467.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/119.0.366.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.431.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.471.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/113.0.209.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/112.0.113.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.469.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.177.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/125.0.212.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/113.0.306.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/111.0.69.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.123.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/119.0.335.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.472.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.123.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/112.0.80.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/121.0.185.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.194.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/121.0.401.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/118.0.54.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/110.0.100.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/110.0.0.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/117.0.93.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/117.0.147.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.111.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/112.0.430.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/112.0.287.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.412.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/112.0.139.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.23.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.317.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/110.0.422.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/118.0.28.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/116.0.185.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/121.0.291.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.489.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/116.0.254.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/119.0.384.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/111.0.63.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.401.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/118.0.378.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.34.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/112.0.134.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.126.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/110.0.137.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/110.0.495.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/111.0.230.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.275.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/121.0.205.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.201.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/121.0.153.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/118.0.477.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.373.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/112.0.452.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/118.0.82.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.496.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.401.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/110.0.433.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/112.0.450.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/119.0.55.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.33.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/121.0.141.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.212.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.397.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/116.0.406.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/113.0.417.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/113.0.276.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.229.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/119.0.116.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.123.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/111.0.10.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/119.0.115.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/119.0.280.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/112.0.198.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.22.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/118.0.153.0 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/119.0.316.0 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.131.0 Safari/604.1"
]

# Đường dẫn file
auth_file = 'user.txt'

# Định nghĩa danh sách màu sắc cho banner
colors = [Fore.YELLOW, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

# ASCII art cho banner
ascii_art = [
    "   ███████╗ ██████╗ ██████╗ ██████╗ ███████╗",
    "   ██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝",
    "   ███████╗██║     ██║   ██║██║  ██║█████╗  ",
    "   ╚════██║██║     ██║   ██║██║  ██║██╔══╝  ",
    "   ███████║╚██████╗╚██████╔╝██████╔╝███████╗",
    "   ╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝"
]

# Khởi tạo cloudscraper
scraper = cloudscraper.create_scraper()

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i, line in enumerate(ascii_art):
        color = colors[i % len(colors)]
        print(f"{color}{Style.BRIGHT}{line}{Fore.RESET}")
    print(f"{Fore.CYAN}{Style.BRIGHT}{'═' * 60}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}          🌟 GOLIKE TOOL PRO v2.5 🌟")
    print(f"{Fore.CYAN}{Style.BRIGHT}{'═' * 60}")
    print(f"{Fore.GREEN}{Style.BRIGHT} 👨‍💻 Tác giả : VAN DAT")
    print(f"{Fore.GREEN}{Style.BRIGHT} 📞 Zalo   : https://zalo.me/g/nexigi855")
    print(f"{Fore.GREEN}{Style.BRIGHT} 🛠 Loại   : Auto golike LinkedIn")
    print(f"{Fore.CYAN}{Style.BRIGHT}{'═' * 60}")

def countdown(time_sec):
    for i in range(time_sec, -1, -1):
        print(f"\r{Fore.YELLOW}{Style.BRIGHT}[⏳] Đang chờ: {i}s{Fore.RESET}", end="")
        time.sleep(1)
    print(f"\r{Fore.GREEN}{Style.BRIGHT}[✅] Đang xử lý...{Fore.RESET}", end="\r")

def create_file_if_not_exists(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write('')
        print(f"{Fore.GREEN}{Style.BRIGHT}[✅] Tạo file {os.path.basename(file_path)} thành công!{Fore.RESET}")

def read_from_file(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
            return content if content else None
    except:
        return None

def write_to_file(file_path, data):
    try:
        with open(file_path, 'w') as f:
            f.write(data)
        return True
    except Exception as e:
        print(f"{Fore.RED}{Style.BRIGHT}[❌] Lỗi khi ghi file: {str(e)}{Fore.RESET}")
        return False

def get_golike_info(headers, retries=3):
    for attempt in range(retries):
        try:
            response = scraper.get('https://gateway.golike.net/api/users/me', headers=headers, timeout=5)
            data = response.json()
            if data['status'] == 200:
                return data['data']['username'], data['data']['coin']
            return "Không xác định", 0
        except Exception as e:
            print(f"{Fore.RED}{Style.BRIGHT}[❌] Lỗi kết nối: {str(e)}. Thử lại sau 5s... ({attempt+1}/{retries}){Fore.RESET}")
            time.sleep(5)
    print(f"{Fore.RED}{Style.BRIGHT}[❌] Không thể kết nối sau {retries} lần thử!{Fore.RESET}")
    return "Lỗi kết nối", 0

def input_auth_token():
    saved_auth = read_from_file(auth_file)
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json;charset=utf-8',
        'Authorization': '',
        'User-Agent': random.choice(USER_AGENTS), 
        'Referer': 'https://app.golike.net/'
    }
    
    while True:
        if saved_auth:
            print(f"{Fore.CYAN}{Style.BRIGHT} [ℹ️] Authorization đã lưu: {saved_auth[:20]}...{Fore.RESET}")
            use_saved = input(f"{Fore.YELLOW}{Style.BRIGHT}[❓] Sử dụng lại thông tin cũ? (y/n): {Fore.RESET}").lower()
            if use_saved == 'y':
                headers['Authorization'] = saved_auth
                username, balance = get_golike_info(headers)
                if username != "Lỗi kết nối" and username != "Không xác định":
                    return headers, username, balance
                else:
                    print(f"{Fore.RED}{Style.BRIGHT}[❌] Thông tin cũ không hợp lệ!{Fore.RESET}")
        
        auth = input(f"{Fore.YELLOW}{Style.BRIGHT}[❓] Nhập Authorization: {Fore.RESET}").strip()
        headers['Authorization'] = auth
        username, balance = get_golike_info(headers)
        
        if username != "Lỗi kết nối" and username != "Không xác định":
            write_to_file(auth_file, auth)
            return headers, username, balance
        else:
            print(f"{Fore.RED}{Style.BRIGHT}[❌] Authorization không hợp lệ! Vui lòng thử lại.{Fore.RESET}")

def get_linkedin_accounts(headers, retries=3):
    for attempt in range(retries):
        try:
            response = scraper.get('https://gateway.golike.net/api/linkedin-account', headers=headers, timeout=5)
            data = response.json()
            if data['status'] == 200 and data.get('data'):
                return data
            print(f"{Fore.RED}{Style.BRIGHT}[❌] Không lấy được danh sách tài khoản LinkedIn! Thử lại sau 5s... ({attempt+1}/{retries}){Fore.RESET}")
            time.sleep(5)
        except Exception as e:
            print(f"{Fore.RED}{Style.BRIGHT}[❌] Lỗi kết nối API: {str(e)}. Thử lại sau 5s... ({attempt+1}/{retries}){Fore.RESET}")
            time.sleep(5)
    print(f"{Fore.RED}{Style.BRIGHT}[❌] Không thể lấy danh sách tài khoản sau {retries} lần thử!{Fore.RESET}")
    return None

def nhannv(account_id, headers, retries=3):
    params = {'account_id': account_id, 'data': 'null'}
    for attempt in range(retries):
        try:
            response = scraper.get('https://gateway.golike.net/api/advertising/publishers/linkedin/jobs', 
                                  params=params, headers=headers, timeout=5)
            return response.json()
        except Exception as e:
            print(f"{Fore.RED}{Style.BRIGHT}[❌] Lỗi khi lấy nhiệm vụ: {str(e)}. Thử lại sau 5s... ({attempt+1}/{retries}){Fore.RESET}")
            time.sleep(5)
    return {'status': 500}

def hoanthanh(ads_id, account_id, headers, retries=3):
    json_data = {'ads_id': ads_id, 'account_id': account_id, 'async': True, 'data': None}
    for attempt in range(retries):
        try:
            response = scraper.post('https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs', 
                                    headers=headers, json=json_data, timeout=5)
            return response.json()
        except Exception as e:
            print(f"{Fore.RED}{Style.BRIGHT}[❌] Lỗi khi hoàn thành: {str(e)}. Thử lại sau 5s... ({attempt+1}/{retries}){Fore.RESET}")
            time.sleep(5)
    return {'status': 500}

def baoloi(ads_id, object_id, account_id, loai, headers):
    json_data = {'ads_id': ads_id, 'object_id': object_id, 'account_id': account_id, 'type': loai}
    try:
        scraper.post('https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs', 
                     headers=headers, json=json_data, timeout=5)
    except Exception as e:
        print(f"{Fore.RED}{Style.BRIGHT}[❌] Lỗi khi bỏ qua nhiệm vụ: {str(e)}{Fore.RESET}")

def display_task_interface(dem, tong, tien, link, status, account_name):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + Style.BRIGHT + "═" * 60)
    print(f"{Fore.YELLOW}{Style.BRIGHT}          🌟 GOLIKE LINKEDIN TOOL - TRANG NHIỆM VỤ 🌟")
    print(Fore.CYAN + Style.BRIGHT + "═" * 60)
    print(f"{Fore.GREEN}{Style.BRIGHT} 👤 Tài khoản: {account_name}")
    print(Fore.CYAN + Style.BRIGHT + "─" * 60)
    print(f"{Fore.GREEN}{Style.BRIGHT} 📊 Số nhiệm vụ hoàn thành: {dem}")
    print(f"{Fore.GREEN}{Style.BRIGHT} 💰 Tổng tiền kiếm được: {tong:,} coin")
    print(f"{Fore.GREEN}{Style.BRIGHT} 💵 Tiền nhiệm vụ gần nhất: {tien:,} coin")
    print(Fore.CYAN + Style.BRIGHT + "─" * 60)
    print(f"{Fore.GREEN}{Style.BRIGHT} 🔗 Link: {link[:35] + '...' if len(link) > 35 else link}")
    print(f"{Fore.GREEN}{Style.BRIGHT} 📡 Trạng thái: {status}")
    print(Fore.CYAN + Style.BRIGHT + "═" * 60)

def run_tool(headers, accounts, username, balance):
    banner()
    print(Fore.CYAN + Style.BRIGHT + "═" * 60)
    print(f"{Fore.YELLOW}{Style.BRIGHT}          🌟 THÔNG TIN TÀI KHOẢN GOLIKE 🌟")
    print(Fore.CYAN + Style.BRIGHT + "═" * 60)
    print(f"{Fore.GREEN}{Style.BRIGHT} 👤 Tên người dùng   : {username}")
    print(f"{Fore.GREEN}{Style.BRIGHT} 💰 Số dư hiện tại  : {balance:,} coin")
    print(f"{Fore.GREEN}{Style.BRIGHT} 🕒 Cập nhật lúc     : {time.strftime('%H:%M:%S %d/%m/%Y')}")
    print(Fore.CYAN + Style.BRIGHT + "─" * 60)
    print(f"{Fore.CYAN}{Style.BRIGHT} 📋 Danh sách tài khoản LinkedIn:")
    for i, acc in enumerate(accounts['data'], 1):
        print(f"{Fore.GREEN}{Style.BRIGHT} [{i}] {acc['name']} - ID: {acc['id']}")
    print(Fore.CYAN + Style.BRIGHT + "═" * 60)
    
    while True:
        try:
            choice = int(input(f"{Fore.YELLOW}{Style.BRIGHT}[❓] Chọn số tài khoản: {Fore.RESET}"))
            if 1 <= choice <= len(accounts['data']):
                account_id = accounts['data'][choice - 1]['id']
                account_name = accounts['data'][choice - 1]['name']
                break
            print(f"{Fore.RED}{Style.BRIGHT}[❌] Lựa chọn không hợp lệ!{Fore.RESET}")
        except:
            print(f"{Fore.RED}{Style.BRIGHT}[❌] Nhập số hợp lệ!{Fore.RESET}")
    
    delay = input(f"{Fore.YELLOW}{Style.BRIGHT}[❓] Nhập Delay (>15s): {Fore.RESET}").strip() or "10"
    try:
        float(delay)
    except ValueError:
        print(f"{Fore.RED}{Style.BRIGHT}[❌] Thời gian chờ phải là số! Dùng mặc định 10s.{Fore.RESET}")
        delay = "10"
    
    doiacc = float('inf')
    print(f"{Fore.YELLOW}{Style.BRIGHT}[ℹ️] Số lần thất bại để đổi acc: Vô hạn{Fore.RESET}")
    
    dem, tong, checkdoiacc = 0, 0, 0
    while True:
        if checkdoiacc >= doiacc:
            display_task_interface(dem, tong, 0, "N/A", f"{Fore.RED}{Style.BRIGHT}Đổi tài khoản do lỗi liên tục!{Fore.RESET}", account_name)
            time.sleep(3)
            break
        
        display_task_interface(dem, tong, 0, "Đang lấy...", f"{Fore.YELLOW}{Style.BRIGHT}Đang lấy nhiệm vụ...{Fore.RESET}", account_name)
        time.sleep(1)
        
        nhanjob = nhannv(account_id, headers)
        
        if nhanjob['status'] == 200:
            ads_id = nhanjob['data']['id']
            link = nhanjob['data']['link']
            object_id = nhanjob['data']['object_id']
            job_type = nhanjob['data']['type']
            
            if job_type not in ['follow', 'like']:
                baoloi(ads_id, object_id, account_id, job_type, headers)
                continue
            
            display_task_interface(dem, tong, 0, link, f"{Fore.YELLOW}{Style.BRIGHT}Đang thực hiện nhiệm vụ...{Fore.RESET}", account_name)
            countdown(int(float(delay)))
            
            display_task_interface(dem, tong, 0, link, f"{Fore.YELLOW}{Style.BRIGHT}Đang nhận tiền...{Fore.RESET}", account_name)
            time.sleep(1)
            nhantien = hoanthanh(ads_id, account_id, headers)
            
            if nhantien['status'] == 200:
                dem += 1
                tien = nhantien['data']['prices']
                tong += tien
                display_task_interface(dem, tong, tien, link, f"{Fore.GREEN}{Style.BRIGHT}Hoàn thành nhiệm vụ!{Fore.RESET}", account_name)
                checkdoiacc = 0
                time.sleep(2)
            else:
                baoloi(ads_id, object_id, account_id, job_type, headers)
                display_task_interface(dem, tong, 0, link, f"{Fore.RED}{Style.BRIGHT}Nhận tiền thất bại!{Fore.RESET}", account_name)
                checkdoiacc += 1
                time.sleep(2)
        else:
            display_task_interface(dem, tong, 0, "N/A", f"{Fore.RED}{Style.BRIGHT}Lấy nhiệm vụ thất bại! Đợi 20s để thử lại...{Fore.RESET}", account_name)
            countdown(20)  # Chờ 20 giây trước khi thử lại
            continue  # Quay lại vòng lặp để thử lấy nhiệm vụ mới

def main():
    create_file_if_not_exists(auth_file)
    banner()
    headers, username, balance = input_auth_token()
    
    banner()
    print(f"{Fore.CYAN}{Style.BRIGHT} 🎉 Đăng nhập thành công 🎉{Fore.RESET}")
    print(f"{Fore.GREEN}{Style.BRIGHT} 👤 Tên người dùng: {username}")
    print(f"{Fore.GREEN}{Style.BRIGHT} 💰 Số dư: {balance:,} coin")
    
    accounts = get_linkedin_accounts(headers)
    if not accounts:
        print(f"{Fore.RED}{Style.BRIGHT}[❌] Không thể tiếp tục do lỗi lấy danh sách tài khoản!{Fore.RESET}")
        return
    
    run_tool(headers, accounts, username, balance)

if __name__ == "__main__":
    main()