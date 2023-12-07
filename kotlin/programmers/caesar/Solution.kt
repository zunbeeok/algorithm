class Solution {
    fun solution(s: String, n: Int): String {
        var answer:String="";
        //"AzC" + n 2
        // CbE
        // 대소문자를 구별하는가?, z이후에 N을 더하게 되면어떻게 처리할래?
        for (v in s){
            var tempAscii:Int = v.toInt();
            //메모리에 어떻게 적재되지?
            // string -> hex -> Decimal

            //buffer란? (hex)
            var asciiNum:Int=0;
            string -> int?



            //알파벳일 경우
            if((65<=tempAscii && tempAscii<=90) || (97<=tempAscii&& tempAscii<=122) ){
                //대문자인 경우.
                if( 65<=tempAscii && tempAscii<=90){
                    asciiNum = tempAscii+n
                    //A-Z 범위를 초과 했을때
                    if (asciiNum >90){
                        asciiNum = asciiNum - 26;
                    }
                }
                //소문자일 경우
                if( 97 <= tempAscii && tempAscii <=122){
                    asciiNum = tempAscii+n
                    //A-Z 범위를 초과 했을때
                    if (asciiNum >122){
                        asciiNum = asciiNum - 26;
                    }
                }
                answer += asciiNum.toChar();
            }else{
                //알파벳이 아닌경우
                answer += v;
            }
        }
        return answer
    }
}