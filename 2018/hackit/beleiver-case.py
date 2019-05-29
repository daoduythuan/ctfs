from flask import Flask, render_template, render_template_string
app = Flask(__name__)
def blacklist_replace(template):
    blacklist = ["[","]","config","self","from_pyfile","|","join","mro","class","request","pop","attr","args","+"]
    for b in blacklist:
        if b in template:
           template=template.replace(b,"")
    return template
@app.route("/")
def index_template():
    return "Hello! I have been contacted by those who try to save the network. I tried to protect myself. Can you test out if I am secure now? <a href='/test'>See this</a>"
@app.route("/<path:template>")
def blacklist_template(template):
	if len(template) > 10000:
        return "This is too long"
    while blacklist_replace(template) != template:
        template = blacklist_replace(template)
    return render_template_string(template)
if __name__ == '__main__':
    app.run(debug=False)
