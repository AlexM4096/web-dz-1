from flask import render_template, redirect, url_for
from app.forms import bp
from app.forms.feedback import Feedback

@bp.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = Feedback()

    if form.validate_on_submit():
        print(form.data)
        return redirect(url_for('main.index'))

    return render_template('forms/feedback.html', form=form)