// import i18next from 'i18next';
// import i18nextXHRBackend from 'i18next-xhr-backend';

i18next
  .use(i18nextXHRBackend)
  .init({
    load: ['ua','en'],
    fallbackLng: 'ua',
    backend: {
      loadPath: '/static/locales/{{lng}}.json'
    }
  }, function(err, t) {
    changeLang("en");
  });

function updateContent() {
    $(".translated").each(function(index) {
        console.log($(this).attr('id'))
        console.log(i18next.t($(this).attr('id')))
        $(this).html(i18next.t($(this).attr('id')))
    })
}

function changeLang(lng) { 
    i18next.changeLanguage(lng);
    updateContent();
}