from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length


class userform(FlaskForm):
    firstname = StringField(
        validators=[
            InputRequired(),
            Length(min=4, max=200),
        ],
        render_kw={"placeholder": "Primer Nombre"},
    )

    lastname = StringField(
        validators=[
            InputRequired(),
            Length(min=4, max=200),
        ],
        render_kw={"placeholder": "Primer Apellido"},
    )

    email = StringField(
        validators=[
            InputRequired(),
            Length(min=4, max=200),
        ],
        render_kw={"placeholder": "Correo Electronico"},
    )

    message = StringField(
        validators=[
            InputRequired(),
            Length(min=4, max=300),
        ],
        render_kw={"placeholder": "Feedback"},
    )

    submit = SubmitField("Enviar")
