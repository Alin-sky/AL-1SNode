function MiddleBg(obj){
    this.id = obj.id;
    this.imgsrc = obj.imgsrc;
    this.bgimgDOM = document.getElementById(this.id);
    this.bgimg = new Image();
    this.bgimg.src = this.imgsrc;
}

MiddleBg.prototype = {
    init: function(){
        let innbgshadow = document.createElement('div');
        innbgshadow.className = 'bgshadow';
        innbgshadow.innerHTML = ''
        this.bgimgDOM.appendChild(innbgshadow);

        this.bgimgDOM.className = 'bgimg';
        let styleEle = document.createElement('style');

        // es6 模板字符串，不了解的请自行查阅
        styleEle.innerHTML = `.${this.bgimgDOM.className},.${this.bgimgDOM.className} .bgshadow {
          height: 100%;
        }
        .${this.bgimgDOM.className}{
            background: url('${this.imgsrc}') no-repeat center;
        }
        .${this.bgimgDOM.className} .bgshadow {
          display: flex;
          align-items: center;
          justify-content: center;
          color: #fff;
          font-size: 5em;
          background: rgba(68, 68, 68, .4);
        }`;
        this.bgimgDOM.appendChild(styleEle);
    },
    resizeListener: function(){
        if (window.innerWidth / window.innerHeight >= this.bgimg.naturalWidth / this.bgimg.naturalHeight) {
            this.bgimgDOM.style.backgroundSize = '100% auto';
        } else {
            this.bgimgDOM.style.backgroundSize = 'auto 100%';
        }
    },
    bgRender: function(){
        // onload 确保图片资源已加载以获取图片原始大小，再进行箭头函数中的操作
        window.onload = ()=>{ // es6 箭头函数，不了解的请自行查阅
            this.init();
            this.resizeListener();
        }
        window.onresize = ()=>{ // 添加监听事件，在此处使用箭头函数，防止this指向window
            this.resizeListener();
        }
    }
}