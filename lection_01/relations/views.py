from django.shortcuts import render, redirect, get_object_or_404
from relations.forms import PersonForm, RatingForm, CommentForm
from relations.models import SinglePerson, Rating, Comment


# Create your views here.
def home_page(request):
    form = PersonForm()
    context = {'form': form}
    return render(request, template_name='relations/home_page.html', context=context)


def user_creation(request):
    new_person = PersonForm(request.POST or None)
    if new_person:
        new_person.save()
        context = {'form': new_person}
        return render(request, template_name='relations/user_created.html', context=context)

    context = {'form': new_person}
    return render(request, template_name='relations/home_page.html', context=context)


def show_persons(request):
    all_persons = SinglePerson.objects.all().order_by('id')
    rating = RatingForm()
    comment_form = CommentForm()

    context = {
        'all_persons': all_persons,
        'rating_form': rating,
        'comment_form': comment_form,
    }
    return render(request, template_name='relations/all_persons.html', context=context)


def edit_person_details(request, pk=int):
    current_person = SinglePerson.objects.get(id=pk)
    form = PersonForm(instance=current_person)

    if request.method != 'POST':
        context = {
            'form': form
        }
        return render(request, template_name='relations/edit_person_details.html', context=context)
    else:
        form = PersonForm(request.POST, instance=current_person)
        if form.is_valid():
            form.save()
            return redirect('show_persons')


def rate_person(request, person_id):
    person = SinglePerson.objects.get(id=person_id)

    if request.method == 'POST':
        rating_value = request.POST.get('rating')

        if rating_value:
            rating = Rating(client=person, rating=rating_value)
            rating.save()

        return redirect(request.META.get('HTTP_REFERER') + f'#{person_id}')

    return render(request, 'relations/all_persons.html', {'person': person})


def comments(request, person_id):
    person = SinglePerson.objects.get(id=person_id)

    if request.method == 'POST':
        username = request.POST.get('username')
        comment = request.POST.get('comment')
        if username and comment:
            current_comment = Comment(client=person, username=username, comment=comment)
            current_comment.save()

            return redirect(request.META.get('HTTP_REFERER') + f'#{person_id}')
