import sys
import pandas as pd


def main(
    videos_csv_path: str, 
    save_normal_csv_path: str,
    save_defect_csv_path: str,
    duration_limit: int = 40,
):
    print(f"Only get duration less than: {duration_limit}")
    df = pd.read_csv(videos_csv_path)
    df['duration'] = pd.to_timedelta(df['duration'])
    
    # filter videos duration less than limit
    df = df[df['duration']<pd.Timedelta(seconds=duration_limit)]
    
    defect_df = df[
        df['title'].str.contains("車禍") | \
        df['title'].str.contains("事故") | \
        df['title'].str.contains("擦撞") | \
        df['title'].str.contains("相撞") | \
        df['title'].str.contains("肇事") | \
        df['title'].str.contains("事故") | \
        df['title'].str.contains("擊落") | \
        df['title'].str.contains("撞我") | \
        df['title'].str.contains("撞到") | \
        df['title'].str.contains("追撞") | \
        df['title'].str.contains("對撞") | \
        df['title'].str.contains("碰到") | \
        df['title'].str.contains("撞飛") | \
        df['title'].str.contains("翻車") | \
        df['title'].str.contains("自摔")
    ]
    normal_df = df[~df['title'].isin(defect_df['title'].tolist())]

    print(f"# of defect: {len(defect_df)}")
    print(f"# of normal: {len(normal_df)}")
    
    defect_df.to_csv(save_defect_csv_path, index=False)
    normal_df.to_csv(save_normal_csv_path, index=False)


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print(
            "Please input follow in argv by order: " + \
            "python3 split_normal_defect_video.py " + \
            "<Video csv file> <Normal video path you want to save> " + \
            "<Defect video path you want to save> " + \
            "<Video duration limit> "
        )
        exit(-1)
    main(sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]))
