// Firebase 共通設定
const firebaseConfig = {
  apiKey: "AIzaSyBqp86LCsX3vGoA3Ug1aBnZbA_oQIVW614",
  authDomain: "quziopus.firebaseapp.com",
  projectId: "quziopus",
  messagingSenderId: "61719920613",
  appId: "1:61719920613:web:a7002a7378c171f98d790c",
  measurementId: "G-FFP3YGKFDT",
  databaseURL: "https://quziopus-default-rtdb.asia-southeast1.firebasedatabase.app/"
};

// Firebase SDK初期化
if (typeof firebase !== 'undefined') {
  firebase.initializeApp(firebaseConfig);
  // Anonymous Auth: ユーザーには見えないが、セキュリティルールで auth != null を満たす
  firebase.auth().signInAnonymously().catch(e => console.warn('Anonymous auth failed:', e));
}

// システム共通のGAS連携URL（メール送信API）
const SYSTEM_GAS_URL = "https://script.google.com/macros/s/AKfycbzCWmgdMJ_a2-oMs08lGu30XBiKhNQrbBFT8mBP2HxuX_g_hnLfk3BQbfMfH-A17eVi/exec";

// セッション管理ヘルパー（localStorageベースに統一）
const session = {
  get(key) { return localStorage.getItem(key); },
  set(key, val) { localStorage.setItem(key, val); },
  clear() {
    const projectId = localStorage.getItem('projectId');
    ['projectId', 'scorer_name', 'scorer_role', 'secretHash', 'adminHash', 'privateKeyJwk'].forEach(k => localStorage.removeItem(k));
    // masterData キャッシュも削除
    if (projectId) localStorage.removeItem(`masterData_${projectId}`);
  },
  get projectId() { return this.get('projectId'); },
  get scorerName() { return this.get('scorer_name'); },
  get scorerRole() { return this.get('scorer_role'); }
};
