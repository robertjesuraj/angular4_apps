import { MyApp1Page } from './app.po';

describe('my-app1 App', () => {
  let page: MyApp1Page;

  beforeEach(() => {
    page = new MyApp1Page();
  });

  it('should display welcome message', done => {
    page.navigateTo();
    page.getParagraphText()
      .then(msg => expect(msg).toEqual('Welcome to app!!'))
      .then(done, done.fail);
  });
});
