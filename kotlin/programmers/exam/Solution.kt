class Solution {

//    fun solution(answers: IntArray): List<Int> {
//        val tempAnswer:Array<Int> = arrayOf(0,0,0)
//        var answer= mutableListOf<Int>();
//        val student1:Array<Int> = arrayOf(1, 2, 3, 4, 5)
//        val student2:Array<Int> = arrayOf(2, 1, 2, 3, 2, 4, 2, 5)
//        val student3:Array<Int> = arrayOf(3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
//        for( i in 0 until answers.size){
//            if(student1[(i-1)%student1.size] ==answers[i]) tempAnswer[0]++
//            if(student2[(i-1)%student2.size] ==answers[i]) tempAnswer[1]++
//            if(student3[(i-1)%student3.size] ==answers[i]) tempAnswer[2]++
//        }
//
//        for(i in tempAnswer){
//            if(tempAnswer[i] == tempAnswer.maxOrNull()){
//                answer.add(i+1)
//            }
//        }
//
//        answer.sort()
////        tempAnswer.maxOrNull()
//
//        return answer
//    }

    init{

    }

//    fun solution(answers: IntArray): List<Int> {
//        val tempAnswer:Array<Int> = arrayOf(0,0,0)
//        var answer= mutableListOf<Int>();
//        val student1:Array<Int> = arrayOf(1, 2, 3, 4, 5)
//        val student2:Array<Int> = arrayOf(2, 1, 2, 3, 2, 4, 2, 5)
//        val student3:Array<Int> = arrayOf(3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
//        for( i in answers.indices){
//            if(student1[i%student1.size] ==answers[i]) tempAnswer[0]++
//            if(student2[i%student2.size] ==answers[i]) tempAnswer[1]++
//            if(student3[i%student3.size] ==answers[i]) tempAnswer[2]++
//        }
//
//            for(i in tempAnswer){
//                if(tempAnswer[i] == tempAnswer.maxOrNull()){
//                    answer.add(i+1)
//                }
//            }
//
//        answer.sort()
////        tempAnswer.maxOrNull()
//
//        return answer
//    }


    //해결한코드

    fun solution(answers: IntArray): List<Int> {
        var tempAnswer:Array<Int> = arrayOf(0,0,0)
        var answer= mutableListOf<Int>();
        var student1:Array<Int> = arrayOf(1, 2, 3, 4, 5)
        var student2:Array<Int> = arrayOf(2, 1, 2, 3, 2, 4, 2, 5)
        var student3:Array<Int> = arrayOf(3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
        for( i in answers.indices){
            if(student1[i%student1.size] ==answers[i]) tempAnswer[0]++
            if(student2[i%student2.size] ==answers[i]) tempAnswer[1]++
            if(student3[i%student3.size] ==answers[i]) tempAnswer[2]++
        }

        for(i in tempAnswer.indices){
            if(tempAnswer[i] == tempAnswer.maxOrNull()){
                answer.add(i+1)
            }
        }

        answer.sort()

        return answer
    }

}