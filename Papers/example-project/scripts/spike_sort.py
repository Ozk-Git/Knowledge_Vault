# spike_sort.py — tip-recording スパイクソーティング
# tags: #example
#
# 使い方:
#   python spike_sort.py --input data/2025-01-15_tiprec.csv --output results/fig1a_tiprec.png
#
# 依存: numpy, scipy, matplotlib

import argparse
import numpy as np
# import matplotlib.pyplot as plt  # 実際の解析時に有効化


def load_recording(path: str) -> np.ndarray:
    """CSV から電位記録を読み込む（時刻[s], 電圧[mV] の2列）"""
    # data = np.loadtxt(path, delimiter=",", skiprows=1)
    # return data
    raise NotImplementedError("実際のデータパスに合わせて実装する")


def detect_spikes(signal: np.ndarray, threshold: float = 0.1) -> np.ndarray:
    """閾値を超えたピークをスパイクとして検出する"""
    # peaks, _ = scipy.signal.find_peaks(signal[:, 1], height=threshold)
    # return signal[peaks, 0]  # スパイク時刻を返す
    raise NotImplementedError


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="記録CSVファイルのパス")
    parser.add_argument("--output", required=True, help="出力図のパス")
    parser.add_argument("--threshold", type=float, default=0.1, help="スパイク検出閾値 (mV)")
    args = parser.parse_args()

    recording = load_recording(args.input)
    spikes = detect_spikes(recording, threshold=args.threshold)
    print(f"検出スパイク数: {len(spikes)}")
    # plot_and_save(spikes, args.output)


if __name__ == "__main__":
    main()
