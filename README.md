# 自己フィードバックシステム

## 概要
このシステムは、あなた(Agent)が複数のAgentを演じ分けることで、自己フィードバックループを実現しながら開発を進めるためのものです。

### Agentの役割
- StudentAgent: 提出物を作成する
- SupervisorAgent: 提出物を評価する


## Task Flow
0. 開発ブランチを作成する(BRANCH_NAMEは自分で決めてください)
```
0-1. git branch
0-2. git checkout main
0-3. git checkout -b feature/BRANCH_NAME
```

1. StudentAgentとして、提出物を作成する
```
# submission_{submission_no}.tomlを作成した後に
```

2. SupervisorAgentとして、提出物を評価する
```
# feedback_{feedback_no}.tomlを作成
```

3. feedbackの総合評価の達成度がS/Aになるまで、1と2をfeedbackの繰り返す

4. 実際に変更を作成

5. 開発の進捗をcommitする
conversation/にあるファイルは.gitignoreに記載されており、commitしない
```
git add {file_path}
git commit -m {commit_message}
```

6. 開発の進捗をpushする
```
git push
```

7. 指示を出した人間に対し、システムについてのfeedbackをfile出力する
- path: conversation/roo_feedbacks/feedback_{feedback_no}.txt



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

#### StudentAgentとSupervisorAgentのフィードバックループ
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

#### Supervisor Agent's task flow
1. Read submission file
2. Think feedback by extention Agent as supervisor
3. Write feedback file

### submit・feedbackの実行方法
```
# 1. student
cat conversation/submission/submission_{submission_no}.toml

# 2. supervisor
cat conversation/feedback/feedback_{feedback_no}.toml
```
