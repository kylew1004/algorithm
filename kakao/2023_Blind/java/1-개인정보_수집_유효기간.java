// # https://school.programmers.co.kr/learn/courses/30/lessons/150370

import java.util.*;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        String info = today.replace(".", "");
        int year = Integer.parseInt(info.substring(0,4));
        int month = Integer.parseInt(info.substring(4,6));
        int day = Integer.parseInt(info.substring(6,8));
        
        int cnt = (year * 12 * 28) + (month * 28) + day;
        
        List<Integer> answer = new ArrayList<>();
        
        
        for(int i = 0; i < privacies.length; i++) {
            String[] pSplit = privacies[i].split(" ");
            
            int num = 0;
            for(int j = 0; j < terms.length; j++){
                String[] tSplit = terms[j].split(" ");
                if(pSplit[1].equals(tSplit[0])) {
                    num = Integer.parseInt(tSplit[1]);
                    break;
                }
            }
            
            String[] pInfo = pSplit[0].split("\\.");
            int pyear = Integer.parseInt(pInfo[0]);
            int pmonth = Integer.parseInt(pInfo[1]);
            int pday = Integer.parseInt(pInfo[2]);
            int pcnt = (pyear*12*28) + ((pmonth + num)*28) + pday - 1;
            
            if (pcnt < cnt)
                answer.add(i+1);
        }
        
        
        return answer.stream().mapToInt(integer->integer).toArray();
    }
}