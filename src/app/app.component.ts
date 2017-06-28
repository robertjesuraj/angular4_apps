import { Component } from '@angular/core';
import { FileUploader } from 'ng2-file-upload';
import { Hero } from './hero';
import { HeroService } from './hero.service';
import { OnInit } from '@angular/core';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [HeroService]
})



export class AppComponent implements OnInit{
  title = 'Angular4 raja try';
  subTitle = 'this is the sub title'


  heroes: Hero[];
  selectedHero: Hero;

  constructor(private heroService: HeroService) { }

  getHeroes(): void {
    //this.heroService.getHeroes().then(heroes => this.heroes = heroes);
    this.heroService.getHeroesSlowly().then(heroes => this.heroes = heroes); // for slow delivery of result
  }

  onSelect(hero: Hero): void {
    this.selectedHero = hero;
  }

  ngOnInit(): void {
    this.getHeroes();
  }

public uploader:FileUploader = new FileUploader({url:'http://localhost:5000/rest/upload'});
}
