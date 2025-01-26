# 自己フィードバックシステム

## 概要
このシステムは、一つのAIが学習者（StudentAgent）と指導者（SupervisorAgent）の二役を演じることで、自己フィードバックループを実現します。

## システムの仕組み

### エージェントの役割

1. StudentAgent
   - フィードバックファイルを読み込む
   - フィードバックに基づいて改善を考える
   - 新しい提出物を作成する

2. SupervisorAgent
   - 学習者の提出物を読み込む
   - 提出内容について評価・分析する
   - フィードバックを作成する

### Rules

```
[StudentAgent] → 提出物作成 → [ファイル] → 読み込み → [SupervisorAgent]
                                                    ↓
                                                  評価
                                                    ↓
[StudentAgent] ← 読み込み ← [ファイル] ← フィードバック作成
```

#### Student Agent's task flow
0. Read feedback file
1. Think Idea by extention Agent as student
2. Submit file by extention Agent as student
3. run student endpoint with submission file path

#### Supervisor Agent's task flow
1. Read submission file
2. Think feedback by extention Agent as supervisor
3. Write feedback file
4. run supervisor endpoint with feedback file path

### submit・feedbackのpythonの実行方法
```
# 1. student
uv run main.py submit conversation/submission/submission_{submission_no}.txt

# 2. supervisor
uv run main.py feedback conversation/feedback/feedback_{feedback_no}.txt
```
