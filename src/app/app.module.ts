import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms'

import { AppComponent } from './app.component';
import { HeroDetailComponent } from './hero-detail.component';

// import { SimpleDemoDirective }    from './simple-demo.directive';
import { FileSelectDirective, FileDropDirective } from 'ng2-file-upload';
// import { FileUploadDemoComponent } from './file-upload-demo.component';

@NgModule({
  declarations: [
    AppComponent,
    FileSelectDirective,
    HeroDetailComponent
  ],
  imports: [
    BrowserModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
