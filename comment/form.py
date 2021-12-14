from django import forms

SITE_SYSTEMS = [
    ('Wordpress', 'وردپرس'),
    ('PrestaShop', 'پرستاشاپ'),
    ('Drupal', 'دروپال'),
    ('Joomla', 'جوملا'),
    ]

BUDGET_AMOUNTS = [
    ('کمتر از ده میلیون تومان', 'کمتر از ده میلیون تومان'),
    ('بین 10 تا 20 میلیون تومان', 'بین 10 تا 20 میلیون تومان'),
    ('بین 35 تا 50 میلیون تومان', 'بین 35 تا 50 میلیون تومان'),
    ('بیش از 70 میلیون تومان', 'بیش از 70 میلیون تومان'),
    ]

WHO_SUPPORTS = [
    ('yes,your team', 'بله،پشتیبانی توسط تیم وب آسا انجام شود.'),
    ('no, our team', 'خیر، تیم پشتیبانی شرکت آن را پشتیبانی خوتهد کرد.'),
    ('not at all', 'کلا قصد پشتیبانی از وب سایت را ندارم'),
    ]

CONTENT_TECHNICAL = [
    ('content support', 'پشتیبانی محتوایی'),
    ('tech support', 'پشتیبانی فنی'),
    ]


class NewComment(forms.Form):
    site_name = forms.CharField(label='نام سایت خود را وارد کنید:',
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": ""})
    )


    host = forms.CharField(label='برای تهیه فضای میزبانی قصد دارید خودتان خریداری کنید یا توسط ما انجام شود؟',
                                widget=forms.TextInput(
                                    attrs={"class": "form-control", "placeholder": ""})
                                )


    your_post = forms.CharField(label='سمت شما در شرکت/مجموعه چیست؟',
                          widget=forms.TextInput(
                              attrs={"class": "form-control", "placeholder": ""})
                          )

    cooperation = forms.CharField(label='برای طراحی سایت خود با شخص یا شرکتی همکاری داشته اید؟ دلیل قطع همکاری',
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": ""}))


    web_design = forms.CharField(label='آیا قبلا سابقه همکاری یا تجربه همکاری با یک طراح سایت را داشتخ اید؟',
                                widget=forms.TextInput(
                                    attrs={"class": "form-control", "placeholder": ""})
                                )

    site_system = forms.CharField(label='قصد طراحی سایت با چه سیستم مدیریت محتوایی را دارید؟',
                                  widget=forms.RadioSelect(choices=SITE_SYSTEMS))

    work_field = forms.CharField(label='در چه زمینه ای قصد فعالیت دارید؟',
                                 widget=forms.TextInput(
                                     attrs={"class": "form-control", "placeholder": ""})
                                 )

    budget = forms.CharField(label='بودجه ای که برای طراحی سایت اختصاص داده اید چقدر است؟',
                                 widget=forms.TextInput(
                                     attrs={"class": "form-control", "placeholder": ""})
                                 )

    support = forms.CharField(label='آیا سایت شما پس از تحویل نیازمند پشتیبانی است؟',
                             widget=forms.TextInput(
                                 attrs={"class": "form-control", "placeholder": ""})
                             )

    budget_amount = forms.CharField(label='بودجه ای که برای طراحی سایت اختصاص داده اید چقدر است؟',
                                  widget=forms.RadioSelect(choices=BUDGET_AMOUNTS))

    who_support = forms.CharField(label='آیا سایت شما پس از تحویل نیازمند پشتیبانی است؟',
                                  widget=forms.RadioSelect(choices=WHO_SUPPORTS))


    content_technical = forms.CharField(label='تمایل به کدام یک از پشتیبانی ها را دارید؟',
                                    widget=forms.RadioSelect(choices=CONTENT_TECHNICAL))



    details = forms.CharField(label='توضیحات تکمیلی که فکر میکنید باید بدانیم را در این قسمت وارد کنید:',
                                  widget=forms.Textarea(
                                      attrs={"class": "form-control", "placeholder": ""}))

    contacts = forms.CharField(label='اطلاعات تماس تان را وارد کنید تا با شما تماس بگیریم:',
                              widget=forms.Textarea(
                                  attrs={"class": "form-control", "placeholder": ""}))
