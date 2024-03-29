from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = 'appDev'
@app.route('/blog-details')
def blogDetails(): return render_template('dashboard/blog-details.html')
@app.route('/blog')
def blog(): return render_template('dashboard/blog.html')
@app.route('/charts-apexcharts')
def chartsApexcharts(): return render_template('dashboard/charts-apexcharts.html')
@app.route('/charts-chartjs')
def chartsChartjs(): return render_template('dashboard/charts-chartjs.html')
@app.route('/charts-echarts')
def chartsEcharts(): return render_template('dashboard/charts-echarts.html')
@app.route('/components-accordion')
def componentsAccordion(): return render_template('dashboard/components-accordion.html')
@app.route('/components-alerts')
def componentsAlerts(): return render_template('dashboard/components-alerts.html')
@app.route('/components-badges')
def componentsBadges(): return render_template('dashboard/components-badges.html')
@app.route('/components-breadcrumbs')
def componentsBreadcrumbs(): return render_template('dashboard/components-breadcrumbs.html')
@app.route('/components-buttons')
def componentsButtons(): return render_template('dashboard/components-buttons.html')
@app.route('/components-cards')
def componentsCards(): return render_template('dashboard/components-cards.html')
@app.route('/components-carousel')
def componentsCarousel(): return render_template('dashboard/components-carousel.html')
@app.route('/components-list-group')
def componentsListgroup(): return render_template('dashboard/components-list-group.html')
@app.route('/components-modal')
def componentsModal(): return render_template('dashboard/components-modal.html')
@app.route('/components-pagination')
def componentsPagination(): return render_template('dashboard/components-pagination.html')
@app.route('/components-progress')
def componentsProgress(): return render_template('dashboard/components-progress.html')
@app.route('/components-spinners')
def componentsSpinners(): return render_template('dashboard/components-spinners.html')
@app.route('/components-tabs')
def componentsTabs(): return render_template('dashboard/components-tabs.html')
@app.route('/components-tooltips')
def componentsTooltips(): return render_template('dashboard/components-tooltips.html')
@app.route('/dashboard')
def dashboard(): return render_template('dashboard/dashboard.html')
@app.route('/forms-editors')
def formsEditors(): return render_template('dashboard/forms-editors.html')
@app.route('/forms-elements')
def formsElements(): return render_template('dashboard/forms-elements.html')
@app.route('/forms-layouts')
def formsLayouts(): return render_template('dashboard/forms-layouts.html')
@app.route('/forms-validation')
def formsValidation(): return render_template('dashboard/forms-validation.html')
@app.route('/icons-bootstrap')
def iconsBootstrap(): return render_template('dashboard/icons-bootstrap.html')
@app.route('/icons-boxicons')
def iconsBoxicons(): return render_template('dashboard/icons-boxicons.html')
@app.route('/icons-remix')
def iconsRemix(): return render_template('dashboard/icons-remix.html')
@app.route('/inner-page')
def innerPage(): return render_template('dashboard/inner-page.html')
@app.route('/pages-blank')
def pagesBlank(): return render_template('dashboard/pages-blank.html')
@app.route('/contactUs')
def contactUs(): return render_template('contactUs.html')
@app.route('/tables-data')
def tablesData(): return render_template('dashboard/tables-data.html')
@app.route('/tables-general')
def tablesGeneral(): return render_template('dashboard/tables-general.html')
@app.route('/users-profile')
def usersProfile(): return render_template('dashboard/users-profile.html')
@app.route('/index-2')
def index2(): return render_template('index-2.html')
@app.route('/index-3')
def index3(): return render_template('index-3.html')
@app.route('/index-4')
def index4(): return render_template('index-4.html')
@app.route('/home')
def index(): return render_template('index.html')
@app.route('/')
def home(): return redirect(url_for('index'))
@app.route('/logIn')
def logIn(): return render_template('logIn.html')
@app.errorhandler(404)
def page404(e): return render_template('page404.html'), 404
@app.route('/FAQ')
def pagesFaq(): return render_template('FAQ.html')
@app.route('/portfolio-details')
def portfolioDetails(): return render_template('portfolio-details.html')
if __name__ == '__main__':
	app.run(debug=True, port=80)