// https://school.programmers.co.kr/learn/courses/30/lessons/42578

import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        
        HashMap<String, Integer> hm = new HashMap<String, Integer>();
        for(String[] clothe : clothes){
            String key = clothe[1];
            hm.put(key, hm.getOrDefault(key, 0) + 1);
        }

        for(String key : hm.keySet()){
            answer *= (hm.get(key) + 1);
        }
        return answer-1;
    }
}