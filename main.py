from flask import Flask, render_template, redirect, make_response, jsonify
from data import db_session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from data.tables import User, Tax, Work
from forms.user_form import UserForm, UpdateUserForm
from forms.login_form import LoginForm
# from forms.article_form import ArticleForm, EditArticleForm, AddTeg
# from forms.message_form import MessageForm
# from forms.news_form import NewsForm
# from flask_restful import Api
# import articles_resources
# import user_resources
# import news_resources
# from requests import post, get, delete, put
# import markdown
# from mail import MAIL
# import TOKEN

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'
# api = Api(app)
login_manager = LoginManager()
login_manager.init_app(app)
# imn = 2


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


# Функция вызова главной страницы сайта

@app.route("/")
def index():
    return render_template("home_page.html", title="Home Page")

# Регистрация пользователя
@app.route("/registration", methods=['GET', 'POST'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.s_name.data,
            name=form.f_name.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('registration.html', title='Регистрация', form=form)


# Вход пользователя
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        use = db_sess.query(User).filter(User.email == form.email.data).first()
        if use and use.check_password(form.password.data):
            login_user(use, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


# Выход из аккаунта
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.errorhandler(401)
def not_found(error):
    return render_template("Error.html", title="Не авторизован", error=401)


@app.errorhandler(404)
def not_found(error):
    return render_template("Error.html", title="Не найдено", error=404)


@app.errorhandler(500)
def not_found(error):
    print(error)
    return render_template("Error.html", title="Наша ошибка", error=500)


def main():
    db_session.global_init("db/Work_gen_1.db")
    #
    # api.add_resource(articles_resources.ArticleResource, '/api/v2/art/<int:art_id>')
    # api.add_resource(user_resources.UserResource, '/api/v2/user/<int:user_id>')
    #
    # api.add_resource(articles_resources.ArticleListResource, '/api/v2/list_art')
    # api.add_resource(user_resources.ListUserResource, '/api/v2/list_user')
    #
    # api.add_resource(articles_resources.TegResource, '/api/v2/teg')
    #
    # api.add_resource(news_resources.NewsListResource, '/api/v2/news')

    app.run()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Неожиданное завершение программы из-за ошибки:')
        print(e)
