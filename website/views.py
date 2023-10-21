from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})

def add(request):
    from random import randint

    num_1 = randint(1,10)
    num_2 = randint(1,10)


    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        # Error handling if no form fillout
        if not answer:
            my_answer = "Hey! You forgot to fill out the form"
            color = 'warning'
            return render(request, 'divide.html', {
            'answer':answer,
            'my_answer':my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color':color,
            })

        correct_answer = int(old_num_1) + int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = "Correct!  "  +  old_num_1  +  " + " +  old_num_2 + " = " +  answer
            color = "success"
        else:
            my_answer = "Incorrect! " +  old_num_1  +  " + " +  old_num_2 + " is not " +  answer + ". It is " + str(correct_answer)
            color = "danger"

        return render(request, 'add.html', {
            'answer':answer,
            'my_answer':my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color':color,
            })

    return render(request, 'add.html', {
        'num_1':num_1,
        'num_2':num_2,
    })

def subtract(request):
    from random import randint

    num_a = randint(1,10)
    num_b = randint(1,10) 

    if int(num_a) > int(num_b): num_1 = num_a; num_2 = num_b 
    else: num_1 = num_b; num_2 = num_a


    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        # Error handling if no form fillout
        if not answer:
            my_answer = "Hey! You forgot to fill out the form"
            color = 'warning'
            return render(request, 'divide.html', {
            'answer':answer,
            'my_answer':my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color':color,
            })

        correct_answer = int(old_num_1) - int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = "Correct!  "  +  old_num_1  +  " - " +  old_num_2 + " = " +  answer
            color = "success"
        else:
            my_answer = "Incorrect! " +  old_num_1  +  " - " +  old_num_2 + " is not " +  answer + ". It is " + str(correct_answer)
            color = "danger"

        return render(request, 'subtract.html', {
            'answer':answer,
            'my_answer':my_answer,
            'num_a':num_a,
            'num_b':num_b,
            'num_1':num_1,
            'num_2':num_2,
            'color':color,
            })

    return render(request, 'subtract.html', {
        'num_1':num_1,
        'num_2':num_2,
    })

def divide(request):
    from random import randint

    num_a = randint(1,3)
    num_b = randint(1,3)
    num_c = int(num_a) * int(num_b)

    if num_1 := num_c: num_2 = num_a


    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        # Error handling if no form fillout
        if not answer:
            my_answer = "Hey! You forgot to fill out the form"
            color = 'warning'
            return render(request, 'divide.html', {
            'answer':answer,
            'my_answer':my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color':color,
            })

        correct_answer = int(old_num_1) / int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = "Correct!  "  +  old_num_1  +  " / " +  old_num_2 + " = " +  answer
            color = "success"
        else:
            my_answer = "Incorrect! " +  old_num_1  +  " / " +  old_num_2 + " is not " +  answer + ". It is " + str(correct_answer)
            color = "danger"

        return render(request, 'divide.html', {
            'answer':answer,
            'my_answer':my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color':color,
            })

    return render(request, 'divide.html', {
        'num_1':num_1,
        'num_2':num_2,
    })

def multiply(request):
    from random import randint

    num_1 = randint(1,10)
    num_2 = randint(1,10)


    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        # Error handling if no form fillout
        if not answer:
            my_answer = "Hey! You forgot to fill out the form"
            color = 'warning'
            return render(request, 'divide.html', {
            'answer':answer,
            'my_answer':my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color':color,
            })

        correct_answer = int(old_num_1) * int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = "Correct!  "  +  old_num_1  +  " * " +  old_num_2 + " = " +  answer
            color = "success"
        else:
            my_answer = "Incorrect! " +  old_num_1  +  " * " +  old_num_2 + " is not " +  answer + ". It is " + str(correct_answer)
            color = "danger"

        return render(request, 'multiply.html', {
            'answer':answer,
            'my_answer':my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color':color,
            })

    return render(request, 'multiply.html', {
        'num_1':num_1,
        'num_2':num_2,
    })
