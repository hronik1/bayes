from flask import Flask, render_template, redirect, request, flash
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import SelectField, StringField, ValidationError, RadioField, BooleanField, SubmitField, IntegerField, FormField, validators
from wtforms.validators import Required

from make_bayesian_inference_for_offenders import make_bayesian_inference_offenders

inference_map = {
    'Severity':'c',
    'Race':'r',
    'Repeat Offense':'n',
    'Gender':'s'
}
class ExampleForm(Form):
    select = SelectField(choices=[('Severity','Severity'), ('Gender', 'Gender'), ('Race', 'Race'), ('Repeat Offense', 'Repeat Offense')])

    submit_button = SubmitField('Submit Form')

class BayesForm(Form):

    race_select = SelectField(choices=[('White','White'), ('Non-White', 'Non-White')])
    gender_select = SelectField(choices=[('Male','Male'), ('Female', 'Female')])
    offense_select = SelectField(choices=[('Repeat Offense','Repeat Offense'), ('First Offense', 'First Offense')])
    severity_select = SelectField(choices=[('Severe','Severe'), ('Minor', 'Minor')])

    string_field = StringField('Computed Conditional Probability')
    submit_button = SubmitField('Submit Form')


def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        form = ExampleForm()
        if form.validate_on_submit():
            to_compute = form.select.data
            return redirect('/bayes?to_compute='+form.select.data)
        return render_template('index.html', form=form)

    @app.route('/bayes', methods=['GET', 'POST'])
    def bayes():
        to_compute = request.args.get('to_compute')
        form = BayesForm()
        if form.validate_on_submit():
            form.string_field.data = str(make_bayesian_inference_offenders(inference_map[to_compute], [form.race_select.data=="White", form.gender_select.data=="Male", form.offense_select.data=="Repeat Offense", form.severity_select.data=="Severe"]))
        return render_template('bayes.html', form=form)

    app.config['SECRET_KEY'] = 'devkey'
    app.config['RECAPTCHA_PUBLIC_KEY'] = '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'

    return app



if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0')               