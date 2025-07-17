// firebase.js - Firebase設定とプロバイダー設定
import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.22.0/firebase-app.js';
import { getAuth, GoogleAuthProvider } from 'https://www.gstatic.com/firebasejs/9.22.0/firebase-auth.js';

// Firebase設定
const firebaseConfig = {
  apiKey: "AIzaSyApiM3EVSaJ_P3xjVS-UB2exXDT6lI3DRk",
  authDomain: "fir-test-87458.firebaseapp.com",
  projectId: "fir-test-87458",
  storageBucket: "fir-test-87458.firebasestorage.app",
  messagingSenderId: "562807781193",
  appId: "1:562807781193:web:3559d480d5b371114ccc98"
};

// Firebase初期化
console.log('🔄 Firebase初期化開始...');
const app = initializeApp(firebaseConfig);
console.log('✅ Firebase アプリ初期化完了');

// Firebase Auth初期化
export const auth = getAuth(app);
console.log('✅ Firebase Auth初期化完了');

// Google認証プロバイダー設定
export const provider = new GoogleAuthProvider();

// Google認証プロバイダーの設定
//provider.addScope('email');
//provider.addScope('profile');

// 初期化完了ログ
console.log('🔥 Firebase初期化完了');
console.log('📊 プロジェクトID:', firebaseConfig.projectId);
console.log('🌐 認証ドメイン:', firebaseConfig.authDomain);
console.log('✅ Firebase Auth準備完了');

// Firebase アプリインスタンスもエクスポート（必要に応じて）
export default app;