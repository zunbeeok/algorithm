class Lotto{
    fun solution(lottos: IntArray, win_nums: IntArray):IntArray{
        //내림차 순으로 정렬.
        //굳이 필요없을듯.
//        var lottosList = lottos.sortedArray();
//        var winNumbList = win_nums.sortedArray();

        var hitNum = 0;
        var jokerNum = 0;

        //매칭 시작
        for( lottoNum in lottos){

            //0 (조커) 인 경우.
            if (lottoNum == 0){
                jokerNum++;
                continue;
            };

            for ( winNum in win_nums){
                //로또가 적중할 경우.
                if(lottoNum == winNum){
                    hitNum++;
                    continue;
                }
            }
        }
        var win:Int = rate(hitNum+jokerNum);
        var lose:Int = rate(hitNum);

        var answer: IntArray = intArrayOf(win,lose);
        return answer;
    }

    //로또 랭크로 변환 시켜주는 함수.
    fun rate(v:Int):Int{
        var rank:Int;
        if(v == 6){
            rank =1;
        }else if(v == 5){
            rank =2;
        }else if(v == 4){
            rank =3;
        }else if(v == 3){
            rank =4;
        }else if(v == 2){
            rank =5;
        }else{
            rank =6;
        }

        return rank;
    }
}