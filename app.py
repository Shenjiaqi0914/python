from flask import Flask, render_template


app = Flask(__name__)

@app.route('/time', methods=['POST'])
def do_search() -> 'html':
    return render_template('results.html',
                            the_title='孕妇产假时间数据')

@app.route('/GDP',methods=['POST'])
def hello() ->'html':
    return render_template('GDP.html',
                           the_title='世界GDP指数数据')

@app.route('/death',methods=['POST'])
def death() ->'html':
    return render_template('death.html',
                           the_title='孕妇死亡率数据')

@app.route('/education',methods=['POST'])
def education() ->'html':
    return render_template('education.html',
                           the_title='中国高等教育率数据')

@app.route('/conclusion',methods=['POST'])
def conclusion() ->'html':
    return render_template('conclusion.html'
                           )

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='产假时间长度跟地区发展程度 经济状况的关联 对女性的社会地位问题进行一个思考')


if __name__ == '__main__':
    app.run(debug=True)
