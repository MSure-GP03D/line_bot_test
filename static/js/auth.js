// auth.js - シンプル版Firebase認証
import { 
  signInWithPopup, 
  signOut, 
  onAuthStateChanged 
} from 'https://www.gstatic.com/firebasejs/9.22.0/firebase-auth.js';
import { auth, provider } from '/static/js/firebase.js';

// Googleポップアップ認証
export const signInWithGoogle = async () => {
  try {
    const result = await signInWithPopup(auth, provider);
    console.log("Firebase result:", result.user)
    const user = result.user;
    const token = await user.getIdToken(); // FirebaseのIDトークン取得
    console.log("Firebase Token:", token);
    console.log("Firebase authentication successful:", user.email);
    
    // Django API呼び出しを別のtry-catchで処理
    try {
      const response = await fetch("/protected/", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
      });
      const data = await response.json();
      console.log("Django API Response:", data);
      
      return { success: true, user, token, data };
    } catch (apiError) {
      console.error("Django API Error:", apiError);
      // Django APIが失敗してもFirebase認証は成功として扱う
      return { success: true, user, token, apiError };
    }
    
  } catch (error) {
    console.error("Authentication Error:", error);
    
    // ポップアップが閉じられた場合は警告として扱う
    if (error.code === 'auth/popup-closed-by-user') {
      console.warn("Popup was closed by user, but this is not a critical error");
      return { success: false, error, isCancelled: true };
    }
    
    // ポップアップがブロックされた場合
    if (error.code === 'auth/popup-blocked') {
      console.warn("Popup was blocked by browser");
      return { success: false, error, isBlocked: true };
    }
    
    // その他のエラー
    return { success: false, error };
  }
};

// ログアウト
export const signOutUser = async () => {
  try {
    await signOut(auth);
    console.log("Logout successful");
    return { success: true };
  } catch (error) {
    console.error("Logout Error:", error);
    return { success: false, error };
  }
};

// 認証状態監視
export const onAuthStateChange = (callback) => {
  return onAuthStateChanged(auth, callback);
};

// 現在のユーザー取得
export const getCurrentUser = () => {
  return auth.currentUser;
};

// IDトークン取得
export const getCurrentUserToken = async () => {
  if (!auth.currentUser) {
    return { success: false, error: "No user logged in" };
  }
  
  try {
    const token = await auth.currentUser.getIdToken();
    return { success: true, token };
  } catch (error) {
    console.error("Token Error:", error);
    return { success: false, error };
  }
};