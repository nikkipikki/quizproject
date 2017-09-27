from django.shortcuts import render



quizzes = [
	{
		"quiz_number": 1,
		"name": "Nicole",
		"description": "Hur bra känner du Nicole?"
	},
	{
		"quiz_number": 2,
		"name": "Nicole + Mattias",
		"description": "Vad vet du om Nicole + Mattias?"
	},
	{
		"quiz_number": 3,
		"name": "Mattias",
		"description": "Hur bra känner du Mattias?"
	},
]


def startpage(request):
	context = {
		"quizzes": quizzes,
	}
	return render(request, "start.html", context)

def quiz(request, quiz_number):
	context = {
		"quiz": quizzes[quiz_number - 1],
		"quiz_number": quiz_number,
		}
	return render(request, "quiz.html", context)



def question(request, quiz_number, question_number):
	context = {
		"question_number": question_number,
	    	"question": "Hur många bultar har ölandsbron?",
		"answer1": "12",
	   	"answer2": "66 400",
	    	"answer3": "7 428 954",
	    	"quiz_number": quiz_number,
	}
	return render(request, "question.html", context)




def completed(request, quiz_number):
	context = {
	    	"correct": 12,
	    	"total": 20,
		"quiz_number": quiz_number,
	}
	return render(request, "results.html", context)


# Create your views here.
