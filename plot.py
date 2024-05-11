import pandas as pd
import numpy as np

## Replica Size Plots

rashnu_1 = np.mean(
    [
        7500,
        7286,
        7314,
        7400,
        7300,
        7400,
        7500,
        7400,
        7500,
        7400,
        7400,
        7300,
        7500,
        7500,
        7400,
        7500,
        7500,
        1700,
    ]
)
rashnu_3 = np.mean(
    [
        6400,
        6000,
        6300,
        6000,
        6200,
        6300,
        6000,
        6300,
        6300,
        6500,
        6500,
        6500,
        6500,
        6416,
        6421,
        6363,
        6400,
        1600,
    ]
)
rashnu_5 = np.mean(
    [
        4600,
        4600,
        4600,
        4527,
        4573,
        4700,
        4600,
        4600,
        4600,
        4500,
        4600,
        4600,
        4600,
        4600,
        4500,
        4600,
        4596,
        104,
    ]
)
rashnu_10 = np.mean(
    [
        3126,
        3074,
        3100,
        3100,
        3100,
        3100,
        3100,
        3200,
        3300,
        3199,
        3101,
        3200,
        3200,
        3176,
        3224,
        3200,
        3000,
    ]
)

themis_1 = np.mean(
    [
        3800,
        3700,
        3800,
        3800,
        3800,
        3739,
        3761,
        3800,
        3800,
        3700,
        3800,
        3800,
        3700,
        3700,
        3800,
        3800,
        3700,
        200,
    ]
)
themis_3 = np.mean(
    [
        3404,
        3396,
        3400,
        3300,
        3300,
        3300,
        3300,
        3300,
        3400,
        3300,
        3300,
        3400,
        3300,
        3400,
        3300,
        3300,
        3300,
        1300,
    ]
)
themis_5 = np.mean(
    [
        800,
        600,
        800,
        700,
        700,
        600,
        700,
        700,
        700,
        700,
        700,
        700,
        600,
        600,
        700,
        700,
        100,
    ]
)
themis_10 = np.mean(
    [
        700,
        700,
        700,
        700,
        661,
        539,
        700,
        600,
        700,
        700,
        600,
        700,
        600,
        600,
        600,
        600,
    ]
)

hotstuff_1 = np.mean(
    [
        26700,
        26500,
        27100,
        26900,
        26800,
        27200,
        26900,
        11600,
    ]
)
hotstuff_3 = np.mean(
    [
        18600,
        18700,
        18700,
        18628,
        18672,
        18800,
        19100,
        18959,
        19241,
        19000,
        11300,
    ]
)
hotstuff_5 = np.mean(
    [
        14800,
        14500,
        14600,
        14500,
        14659,
        14641,
        14553,
        14747,
        14500,
        14600,
        14600,
        14600,
        14578,
        9822,
    ]
)
hotstuff_10 = np.mean(
    [
        8977,
        9049,
        8974,
        8900,
        8900,
        8950,
        8850,
        8900,
        8900,
        8800,
        8800,
        8985,
        8815,
        8800,
        8862,
        8881,
        8915,
        8997,
        645,
    ]
)

rashnu_network = pd.DataFrame(
    {
        "Rashnu": [
            rashnu_1,
            rashnu_3,
            rashnu_5,
            rashnu_10,
        ],
        "Themis": [
            themis_1,
            themis_3,
            themis_5,
            themis_10,
        ],
        "Hotstuff": [
            hotstuff_1,
            hotstuff_3,
            hotstuff_5,
            hotstuff_10,
        ],
    },
    index=[
        1,
        3,
        5,
        10,
    ],
)


# print(rashnu_network)

ax = rashnu_network.plot.bar(figsize=(10, 10))
ax.set_title("(1) Varying Network Size (Throughput)")
ax.set_ylabel("Throughput (ops/s)")
ax.set_xlabel("f = 1, 3, 5, 10")
fig = ax.get_figure()
fig.savefig("plots/(1)_networksz.png")

rashnu_network_latency = pd.DataFrame(
    {
        "Rashnu": [
            53.812,
            62.633,
            87.135,
            126.726,
        ],
        "Themis": [
            106.178,
            119.783,
            2338.828,
            2465.256,
        ],
        "Hotstuff": [
            14.843,
            21.212,
            27.360,
            44.875,
        ],
    },
    index=[
        1,
        3,
        5,
        10,
    ],
)

ax = rashnu_network_latency.plot.line(figsize=(10, 10))
ax.set_title("(1) Varying Network Size (Latency)")
ax.set_ylabel("Latency (ms)")
ax.set_xlabel("f = 1, 3, 5, 10")
fig = ax.get_figure()
fig.savefig("plots/(1)_networksz_latency.png")


## Network Failure Plots

rashnu_failure_1 = np.mean(
    [
        7600,
        7500,
        7500,
        7400,
        7500,
        7500,
        7500,
        7500,
        7500,
        7500,
        7500,
        7300,
        7500,
        7600,
        7500,
        7600,
        7520,
        6780,
    ]
)

rashnu_failure_3 = np.mean(
    [
        6500,
        6500,
        6500,
        6413,
        6387,
        6400,
        6400,
        6500,
        6400,
        6400,
        6400,
        6400,
        6400,
        6300,
        6400,
        6300,
        6300,
        6200,
        2800,
    ]
)

rashnu_failure_5 = np.mean(
    [
        4500,
        4500,
        4497,
        4403,
        4400,
        4500,
        4500,
        4500,
        4400,
        4500,
        4400,
        4500,
        4500,
        4488,
        4412,
        4500,
        4400,
        923,
    ]
)

rashnu_failure_10 = np.mean(
    [
        3100,
        3000,
        3100,
        3100,
        3100,
        3100,
        3100,
        3200,
        3101,
        3199,
        3100,
        3200,
        3152,
        3148,
        3200,
        3000,
        3100,
    ]
)

themis_failure_1 = np.mean(
    [
        3800,
        3800,
        3800,
        3800,
        3800,
        3744,
        3756,
        3800,
        3700,
        3800,
        3800,
        3700,
        3700,
        3800,
        3700,
        3800,
        3800,
        3700,
        900,
    ]
)
themis_failure_3 = np.mean(
    [
        3400,
        3400,
        3300,
        3300,
        3400,
        3300,
        3300,
        3300,
        3315,
        3285,
        3400,
        3300,
        3300,
        3361,
        3339,
        3300,
        3300,
        800,
    ]
)
themis_failure_5 = np.mean(
    [
        800,
        600,
        800,
        700,
        700,
        600,
        700,
        800,
        700,
        700,
        700,
        700,
        600,
        600,
        700,
        700,
        600,
        200,
    ]
)
themis_failure_10 = np.mean(
    [700, 700, 700, 693, 607, 700, 600, 700, 700, 700, 600, 600, 600, 600, 547, 453]
)

hotstuff_failure_1 = np.mean([27800, 27728, 27941, 27801, 27030, 27400, 27201, 6799])
hotstuff_failure_3 = np.mean(
    [17156, 17244, 17424, 17817, 17259, 16000, 16000, 16700, 16500, 16700, 17000, 13900]
)
hotstuff_failure_5 = np.mean(
    [
        14500,
        14400,
        14400,
        14200,
        14400,
        14600,
        14600,
        14630,
        14704,
        14720,
        14644,
        14502,
        14600,
        10800,
    ]
)
hotstuff_failure_10 = np.mean(
    [
        8800,
        8900,
        8800,
        8771,
        8795,
        8734,
        8800,
        8800,
        8737,
        8763,
        8900,
        8861,
        8839,
        8800,
        8763,
        8748,
        8789,
        8788,
        812,
    ]
)

replica_failure_df = pd.DataFrame(
    {
        "Rashnu No Fail": [rashnu_1, rashnu_3, rashnu_5, rashnu_10],
        "Rashnu Fail": [
            rashnu_failure_1,
            rashnu_failure_3,
            rashnu_failure_5,
            rashnu_failure_10,
        ],
        "Themis No Fail": [themis_1, themis_3, themis_5, themis_10],
        "Themis Fail": [
            themis_failure_1,
            themis_failure_3,
            themis_failure_5,
            themis_failure_10,
        ],
        "Hotstuff No Fail": [hotstuff_1, hotstuff_3, hotstuff_5, hotstuff_10],
        "Hotstuff Fail": [
            hotstuff_failure_1,
            hotstuff_failure_3,
            hotstuff_failure_5,
            hotstuff_failure_10,
        ],
    },
    index=[1, 3, 5, 10],
)

ax = replica_failure_df.plot.line(figsize=(10, 10))
ax.set_title("(2) Replica Failure (Throughput)")
ax.set_ylabel("Throughput (op/s)")
ax.set_xlabel("f = 1, 3, 5, 10")
fig = ax.get_figure()
fig.savefig("plots/(2)_network_failure.png")


replica_failure_latency_df = pd.DataFrame(
    {
        "Rashnu No Fail": [
            53.812,
            62.633,
            87.135,
            126.726,
        ],
        "Rashnu Fail": [
            53.116,
            62.514,
            89.502,
            128.200,
        ],
        "Themis No Fail": [
            106.178,
            119.783,
            2338.828,
            2465.256,
        ],
        "Themis Fail": [
            105.833,
            120.088,
            2328.988,
            2471.148,
        ],
        "Hotstuff No Fail": [
            14.843,
            21.212,
            27.360,
            44.875,
        ],
        "Hotstuff Fail": [
            14.457,
            23.470,
            27.491,
            45.418,
        ],
    },
    index=[1, 3, 5, 10],
)

ax = replica_failure_latency_df.plot.line(figsize=(10, 10))
ax.set_title("(2) Replica Failure (Latency)")
ax.set_ylabel("Latency (ms)")
ax.set_xlabel("f = 1, 3, 5, 10")
fig = ax.get_figure()
fig.savefig("plots/(2)_network_failure_latency.png")


rashnu_block_5 = np.mean(
    [
        490,
        600,
        615,
        595,
        620,
        620,
        625,
        605,
        610,
        620,
        625,
        620,
        620,
        625,
        615,
        625,
        585,
        210,
    ]
)
rashnu_block_25 = np.mean(
    [
        2800,
        2875,
        2900,
        2825,
        2900,
        2900,
        2825,
        2800,
        2900,
        2850,
        2850,
        2850,
        2850,
        2800,
        2725,
        2850,
        2850,
        1400,
    ]
)
rashnu_block_50 = np.mean(
    [
        5450,
        5350,
        5350,
        5300,
        5350,
        5350,
        5250,
        5200,
        5250,
        5250,
        5200,
        5250,
        5300,
        5350,
        5200,
        5250,
        5150,
        5300,
        850,
    ]
)
rashnu_block_100 = np.mean(
    [
        7500,
        7286,
        7314,
        7400,
        7300,
        7400,
        7500,
        7400,
        7500,
        7400,
        7400,
        7300,
        7500,
        7500,
        7400,
        7500,
        7500,
        1700,
    ]
)
rashnu_block_200 = np.mean(
    [
        5000,
        5200,
        5000,
        5000,
        5200,
        5000,
        5000,
        5000,
        5000,
        5200,
        5000,
        4867,
        4933,
        5000,
        4921,
        4879,
        4800,
        5000,
        5000,
        1800,
    ]
)
rashnu_block_400 = np.mean(
    [
        2800,
        2800,
        2800,
        2800,
        3200,
        2800,
        2400,
        2800,
        2800,
        2800,
        2800,
        2800,
        2800,
        2800,
        2400,
        2800,
        2800,
        800,
    ]
)

themis_block_5 = np.mean(
    [
        555,
        640,
        670,
        645,
        670,
        675,
        665,
        640,
        675,
        670,
        670,
        670,
        665,
        665,
        660,
        630,
        670,
        70,
    ]
)
themis_block_25 = np.mean(
    [
        3025,
        3075,
        3075,
        3025,
        3075,
        3025,
        2975,
        3050,
        3050,
        3025,
        3000,
        3025,
        3000,
        2928,
        3047,
        2975,
        3025,
        1075,
    ]
)
themis_block_50 = np.mean(
    [
        5300,
        5300,
        5350,
        5248,
        5302,
        5300,
        5200,
        5150,
        5300,
        5300,
        5150,
        5200,
        5200,
        5250,
        5200,
        5050,
        5050,
        1850,
    ]
)
themis_block_100 = np.mean(
    [
        3800,
        3700,
        3800,
        3800,
        3800,
        3739,
        3761,
        3800,
        3800,
        3700,
        3800,
        3800,
        3700,
        3700,
        3800,
        3800,
        3700,
        200,
    ]
)
themis_block_200 = np.mean(
    [
        2000,
        1800,
        1800,
        2000,
        1800,
        1800,
        1800,
        1992,
        1808,
        1800,
        1800,
        1800,
        1800,
        1800,
        1800,
        2000,
        1800,
        1800,
    ]
)
themis_block_400 = np.mean(
    [
        1200,
        800,
        800,
        800,
        800,
        800,
        800,
        1200,
        800,
        800,
        800,
        800,
        800,
        800,
        800,
        800,
        800,
    ]
)

hotstuff_block_5 = np.mean(
    [
        3755,
        3755,
        3750,
        3745,
        3750,
        3740,
        3690,
        3735,
        3745,
        3750,
        3757,
        3768,
        3805,
        3825,
        3846,
        3750,
        3739,
        2035,
    ]
)
hotstuff_block_25 = np.mean(
    [18518, 18232, 17875, 18136, 18190, 18049, 17996, 18054, 18466, 17784, 17950, 675]
)
hotstuff_block_50 = np.mean([33508, 33092, 33186, 33914, 33800, 32350])
hotstuff_block_100 = np.mean([26700, 26500, 27100, 26900, 26800, 27200, 26900, 11600])
hotstuff_block_200 = np.mean([34400, 33800, 34272, 34110, 33618, 29200])
hotstuff_block_400 = np.mean([38544, 38334, 38625, 37297, 38400, 7600])

blocksz_df = pd.DataFrame(
    {
        "Rashnu": [
            rashnu_block_5,
            rashnu_block_25,
            rashnu_block_50,
            rashnu_block_100,
            rashnu_block_200,
            rashnu_block_400,
        ],
        "Themis": [
            themis_block_5,
            themis_block_25,
            themis_block_50,
            themis_block_100,
            themis_block_200,
            themis_block_400,
        ],
        "Hotstuff": [
            hotstuff_block_5,
            hotstuff_block_25,
            hotstuff_block_50,
            hotstuff_block_100,
            hotstuff_block_200,
            hotstuff_block_400,
        ],
    },
    index=[5, 25, 50, 100, 200, 400],
)

ax = blocksz_df.plot.bar(figsize=(10, 10))
ax.set_title("(3) Block Size (Throughput)")
ax.set_ylabel("Throughput (op/s)")
ax.set_xlabel("block size = 5, 25, 50, 100, 200, 400")
fig = ax.get_figure()
fig.savefig("plots/(3)_blocksz.png")


blocksz_latency_df = pd.DataFrame(
    {
        "Rashnu": [
            646.581,
            139.847,
            75.403,
            53.812,
            159.847,
            574.337,
        ],
        "Themis": [
            599.090,
            131.802,
            76.044,
            106.178,
            435.247,
            1892.005,
        ],
        "Hotstuff": [
            106.625,
            22.041,
            11.859,
            14.843,
            23.410,
            41.681,
        ],
    },
    index=[5, 25, 50, 100, 200, 400],
)

ax = blocksz_latency_df.plot.line(figsize=(10, 10))
ax.set_title("(3) Block Size (Latency)")
ax.set_ylabel("Latency (ms)")
ax.set_xlabel("block size = 5, 25, 50, 100, 200, 400")
fig = ax.get_figure()
fig.savefig("plots/(3)_blocksz_latency.png")


rashnu_geo = np.mean(
    [
        1200,
        1201,
        1299,
        1200,
        1200,
        1286,
        1214,
        1200,
        1200,
        1300,
        1200,
        1200,
        1300,
        1200,
        1233,
        1267,
        1200,
    ]
)
themis_geo = np.mean(
    [
        600,
        600,
        600,
        600,
        600,
        600,
        600,
        600,
        500,
        600,
        600,
        600,
        500,
        600,
        500,
        500,
        400,
    ]
)
hotstuff_geo = np.mean(
    [
        1700,
        1700,
        1700,
        1700,
        1700,
        1700,
        1700,
        1700,
        1700,
        1700,
        1700,
        1700,
        1700,
        1700,
        1700,
        1700,
        1700,
        1700,
        500,
    ]
)


geo_df = pd.DataFrame(
    {
        "Rashnu": [rashnu_block_100, rashnu_geo],
        "Themis": [themis_block_100, themis_geo],
        "Hotstuff": [hotstuff_block_100, hotstuff_geo],
    },
    index=["Clemson", "Distributed"],
)


ax = geo_df.T.plot.bar(figsize=(10, 10))
ax.set_title("(4) Geo Distributed (Throughput)")
ax.set_ylabel("Throughput (op/s)")
ax.set_xlabel("f = 1 ; γ = 1 ; n = 4 ; blocksz = 100")
fig = ax.get_figure()
fig.savefig("plots/(4)_geo.png")


geo_latency_df = pd.DataFrame(
    {
        "Rashnu": [53.812, 324.409],
        "Themis": [106.178, 2771.834],
        "Hotstuff": [14.843, 235.177],
    },
    index=["Clemson", "Distributed"],
)

ax = geo_latency_df.T.plot.line(figsize=(10, 10))
ax.set_title("(4) Geo Distributed (Latency)")
ax.set_ylabel("Latency (ms)")
ax.set_xlabel("f = 1 ; γ = 1 ; n = 4 ; blocksz = 100")
fig = ax.get_figure()
fig.savefig("plots/(4)_geo_latency.png")


rashnu_fairness_60 = np.mean(
    [
        4600,
        4600,
        4600,
        4527,
        4573,
        4700,
        4600,
        4600,
        4600,
        4500,
        4600,
        4600,
        4600,
        4600,
        4500,
        4600,
        4596,
        104,
    ]
)
rashnu_fairness_75 = np.mean(
    [
        6687,
        6700,
        6700,
        6800,
        6700,
        6600,
        6700,
        6700,
        6700,
        6600,
        6600,
        6684,
        6616,
        6700,
        6700,
        6688,
        6712,
        1600,
    ]
)
rashnu_fairness_100 = np.mean(
    [
        7500,
        7286,
        7314,
        7400,
        7300,
        7400,
        7500,
        7400,
        7500,
        7400,
        7400,
        7300,
        7500,
        7500,
        7400,
        7500,
        7500,
        1700,
    ]
)

themis_fairness_60 = np.mean(
    [
        800,
        600,
        800,
        700,
        700,
        600,
        700,
        700,
        700,
        700,
        700,
        700,
        600,
        600,
        700,
        700,
        100,
    ]
)
themis_fairness_75 = np.mean(
    [
        3500,
        3600,
        3500,
        3495,
        3405,
        3500,
        3500,
        3500,
        3500,
        3400,
        3500,
        3600,
        3400,
        3400,
        3500,
        3400,
        3500,
        3432,
        468,
    ]
)
themis_fairness_100 = np.mean(
    [
        3800,
        3700,
        3800,
        3800,
        3800,
        3739,
        3761,
        3800,
        3800,
        3700,
        3800,
        3800,
        3700,
        3700,
        3800,
        3800,
        3700,
        200,
    ]
)

fairness_df = pd.DataFrame(
    {
        "Rashnu": [rashnu_fairness_60, rashnu_fairness_75, rashnu_fairness_100],
        "Themis": [themis_fairness_60, themis_fairness_75, themis_fairness_100],
    },
    index=[0.6, 0.75, 1],
)

ax = fairness_df.plot.bar(figsize=(10, 10))
ax.set_title("(5) Order Fairness Parameter (Throughput)")
ax.set_ylabel("Throughput (op/s)")
ax.set_xlabel(" γ = .60, .75 , 1")
fig = ax.get_figure()
fig.savefig("plots/(5)_fariness.png")

fairness_latency_df = pd.DataFrame(
    {
        "Rashnu": [87.135, 59.818, 53.812],
        "Themis": [2338.828, 114.760, 106.178],
    },
    index=[0.6, 0.75, 1],
)

ax = fairness_latency_df.plot.line(figsize=(10, 10))
ax.set_title("(5) Order Fairness Parameter (Latency)")
ax.set_ylabel("Latency (ms)")
ax.set_xlabel(" γ = .60, .75 , 1")
fig = ax.get_figure()
fig.savefig("plots/(5)_fariness_latency.png")
