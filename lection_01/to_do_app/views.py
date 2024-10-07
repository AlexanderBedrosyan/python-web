from django.forms import modelform_factory, formset_factory
from django.shortcuts import render, HttpResponse, redirect
from .models import ToDoList, Person
from .forms import (NameForm, Url, HelpText, Comment, SelectOptionForm, RadioButtonForm, CheckBoxForm, InheritModelForm,
                    BookForm, PersonForm)

# Create your views here.


def home(request):
    all_tasks = None
    form = NameForm()
    url = Url()
    help_text = HelpText()
    comment = Comment()
    select_option = SelectOptionForm()
    radio_button = RadioButtonForm()
    check_box = CheckBoxForm()
    inherit_model = InheritModelForm()

    if request.GET.get('mybtn'):
        all_tasks = ToDoList.objects.all()
    tasks_content = {
        "tasks": all_tasks,
        "form": form,
        "url": url,
        "help_text": help_text,
        "comment": comment,
        "select_option": select_option,
        "radio_button": radio_button,
        "check_box": check_box,
        "inherit_model": inherit_model
    }

    return render(request, 'base.html', tasks_content)


def task_by_name(request, task_name):


    return HttpResponse(f"Task name is: {task_name}")


def custom_404(request, exception):
    return render(request, '404.html', status=404)


def forms(request):
    context = {}
    form_url = NameForm(request.POST or None)

    if request.method == "POST" and form_url.is_valid():
        entered_name = request.POST.get('name')
        if entered_name:
            print(f"Ima si ime: {entered_name}")
            context['name'] = entered_name
        else:
            print("Няма въведено име!")
    else:
        print('Neshto nI bachi, brat!')

    return render(request, template_name='forms.html', context=context)

def checker(request, current_object, context, name_needed):
    if request.method == "POST" and current_object.is_valid():
        entered_name = request.POST.get(f'{name_needed}')

        if entered_name:
            print(f"Ima si ime: {entered_name}")
            context[f'{name_needed}'] = entered_name
        else:
            print("Няма въведено име!")
    else:
        print('Neshto nI bachi, brat!')

    return context


def diff_form_fields(request):
    context = {}
    url = Url(request.POST or None)
    help_text = HelpText(request.POST or None)
    comment = Comment(request.POST or None)
    select_option = SelectOptionForm(request.POST or None)
    radio_option = RadioButtonForm(request.POST or None)
    check_box = CheckBoxForm(request.POST or None)
    inherit_model = InheritModelForm(request.POST or None)

    context = checker(request, url, context, 'url_path')
    context = checker(request, help_text, context, 'first_name')
    context = checker(request, comment, context, 'comment')
    context = checker(request, select_option, context, "choice_field")
    context = checker(request, radio_option, context, "radio_field")
    context = checker(request, check_box, context, "checkbox_field")
    context = checker(request, inherit_model, context, "title")


    return render(request, template_name='diff_form_fields.html', context=context)


def inheritance_html(request):
    return render(request, template_name='inheritance_base.html')

def test_inherit(request):
    context = {}
    return render(request, template_name='inherit_child.html', context=context)


def custom_tag_example(request):
    return render(request, template_name="custom_tag_examples.html")


def forms_advanced(request):
    form = BookForm(request.POST or None)
    init_form = PersonForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect("forms_advanced.html")

    context = {
        'form': form,
        'init_form': init_form
    }

    return render(request, "forms_advanced.html", context)


def modelform_factory_views(request):
    person = modelform_factory(Person, fields=['first_name', 'last_name', 'birth_date'])
    BookFormSet = formset_factory(BookForm, extra=3)

    if request.method == "POST":
        form = Person(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = person

    if request.method == 'POST':
        formset = BookFormSet(request.POST)
        if formset.is_valid():
            for curr_form in formset:
                if curr_form.cleaned_dat:
                    curr_form.save()
    else:
        formset = BookFormSet

    return render(request, 'modelform_factory.html', {'form': form, 'formset': formset})


BookFormSet = formset_factory(BookForm, extra=3)

def manage_books(request):
    if request.method == 'POST':
        # При пост заявка, събираме и валидираме формите
        formset = BookFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:  # Проверяваме дали формата е попълнена
                    form.save()
    else:
        # При GET заявка, показваме празен formset с 3 празни форми
        formset = BookFormSet()

    return render(request, 'manage_books.html', {'formset': formset})