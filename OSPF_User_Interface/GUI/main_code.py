from flask import Flask, render_template, Markup, request
import getconfig
import ospf_config
import diffconfig
import migration


app = Flask(__name__)
@app.route('/')
def first():
	title = "Welcome. Select one"
	return render_template('index.html', title=title)

@app.route('/get_config')
def second():
	files = getconfig.main()
	return render_template('template.html', files=files), files

@app.route('/OSPF_config')
def third():
	return render_template('temp.html')

@app.route('/details_page', methods=['GET', 'POST'])
def fourth():
	data_config = request.form
	data = ospf_config.main(data_config)	
	return render_template('temp1.html', data=data)

@app.route('/diffconfig', methods=['GET', 'POST'])
def fifth():
	diffconfig.main()
	return render_template('temp2.html')

@app.route('/migration', methods=['GET', 'POST'])
def sixth():
	value = migration.main()
	return render_template('temp3.html', value=value)


if __name__ == '__main__':
	app.debug = True
	app.run(host = '127.0.0.1', port = 80)


