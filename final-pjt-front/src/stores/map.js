import { defineStore } from "pinia";
import { ref } from "vue";
import { KakaoMap } from "vue3-kakao-maps";

export const useMapStore = defineStore("map", () => {
  const API_KEY = 'MY_KAKAO_API'


  return { API_KEY, };
});
