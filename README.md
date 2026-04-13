# QuizOpus

マルチテナント対応のリアルタイム採点プラットフォーム。  
ペーパーテスト（クイズ大会等）の **回答用紙PDF生成 → スキャン → 自動採点 → 成績開示** をブラウザだけで完結させます。

## 🏗 アーキテクチャ

```
Browser (静的HTML/JS)  ──── Firebase Realtime Database
                          ├── projects/{pid}/publicSettings
                          ├── projects/{pid}/entries
                          └── projects/{pid}/protected/{hash}/...
                                ├── config
                                ├── answers (答案画像)
                                ├── answers_text (模範解答)
                                ├── scores (採点データ)
                                └── disclosure (成績開示)
```

## 📁 ファイル構成

```
app/
├── index.html          # ログイン・プロジェクト作成
├── judge.html          # 問題一覧（採点者メインページ）
├── question.html       # 個別問題の採点画面
├── conflict.html       # 採点不一致の確認・確定
├── admin.html          # 管理画面（5タブ構成）
├── checkin.html        # QRコード当日受付
├── entry.html          # エントリーフォーム（公開）
├── entry_list.html     # エントリーリスト（公開）
├── cancel.html         # キャンセルフォーム（公開）
├── disclosure.html     # 成績開示（公開）
├── css/
│   └── design_system.css   # 全ページ共通デザインシステム
├── js/
│   ├── config.js       # Firebase設定 + セッション管理
│   ├── shared.js       # 共通ユーティリティ (認証, Toast, Menu)
│   ├── crypto.js       # RSA暗号化 (個人情報保護)
│   ├── index.js        # ログイン処理
│   ├── judge.js        # 問題一覧ロジック
│   ├── question.js     # 採点ロジック
│   ├── conflict.js     # 不一致解決ロジック  
│   ├── admin.js        # 管理画面ロジック
│   ├── checkin.js      # QR受付ロジック
│   ├── entry.js        # エントリー送信
│   ├── entry_list.js   # エントリーリスト表示
│   ├── cancel.js       # キャンセル処理
│   ├── disclosure.js   # 成績開示表示
│   ├── cv.js           # OpenCV.js ラッパー（答案スキャン用）
│   └── aruco.js        # ArUcoマーカー検出
├── fonts/
│   └── BIZUDGothic-Regular.ttf  # PDF日本語フォント
├── aruco_markers/      # 回答用紙用マーカー画像 (4枚)
├── reference/
│   └── gas_mail_api.js # GAS メール送信APIリファレンス
└── database.rules.json # Firebase セキュリティルール
```

## 🚀 ローカル起動

```bash
cd app
python3 -m http.server 8080
```

http://localhost:8080/index.html にアクセス。

> **注意**: Firebaseへの接続が必要です。オフラインでは動作しません。

## 🔧 Firebase セットアップ

1. [Firebase Console](https://console.firebase.google.com/) でプロジェクトを作成
2. Realtime Database を有効化（リージョン: `asia-southeast1` 推奨）
3. `js/config.js` の `firebaseConfig` を自分のプロジェクトの値に更新
4. `database.rules.json` の内容を Firebase Console のルールに貼り付け

## 📋 運用フロー

1. **プロジェクト作成**: `index.html` → 「新規作成」→ プロジェクト名・管理者名入力
2. **回答用紙発行**: 管理画面 → 採点準備タブ → 問題数設定 → PDF生成
3. **エントリー受付**: 管理画面 → 参加者タブ → 受付ON/期間設定
4. **当日受付**: `checkin.html` → QRコードスキャンで出欠管理
5. **答案スキャン**: 管理画面 → 答案管理タブ → 複合機スキャン画像アップロード
6. **採点**: `judge.html` → 各問題をタップ → 3名で独立採点 → 不一致は確認画面で確定
7. **成績開示**: 管理画面 → 集計タブ → CSV出力 / 成績開示ON

## 📄 ライセンス

Private
