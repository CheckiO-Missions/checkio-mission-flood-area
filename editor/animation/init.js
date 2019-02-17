//Dont change it
requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $, TableComponent) {
        function floodAreaCanvas(dom, input, data) {
            if (! data.ext) {
                return
            }
            const exp = data.ext.explanation
            const result = data.ext.result
            const diagram = input[0]
            const width = diagram.length
            const attr = {
                mountain: {
                    ridge: {
                        'stroke': '#F0801A',
                        'stroke-width': 0.5/(width/20)+'px',
                        'stroke-linejoin': 'round',
                        'stroke-linecap': 'round',
                    },
                    content: {
                        'stroke-width': 0.5/(width/20)+'px',
                        'stroke-linejoin': 'round',
                        'stroke-linecap': 'round',
                        'fill': '#FABA00',
                    }
                },
                grid: {
                    before: {
                        'stroke': '#DFE8F7',
                        'fill':'#DFE8F7',
                        'stroke-width': 0.5/(width/20)+'px',
                    },
                    after: {
                        'stroke': '#2080B8',
                        'fill': '#2080B8',
                        'stroke-width': 0.5/(width/20)+'px',
                    },
                },
                flood: {
                    before: {
                        'fill': '#DFE8F7',
                        'stroke': '#DFE8F7',
                        'stroke-width': 0.5/(width/20)+'px',
                    },
                    after: {
                        'fill': 'skyblue',
                        'stroke': '#2080B8',
                        'stroke-width': 0.5/(width/20)+'px',
                    }
                },
            };

            /*----------------------------------------------*
             *
             * input
             *
             *----------------------------------------------*/
            const area = []
            exp.forEach(([s, e])=>{
                area[s] = e
            })

            let elevation = []
            let min_elevation = 9999
            let max_elevation = -9999
            let cur_rel_elevation = 0

            diagram.split('').forEach((d, i)=>{

                let modify = 0

                if (i > 0) {
                    if (['\\'].includes(d)) {
                        modify = -1
                    } else {
                        modify = 0
                    }

                    if (diagram[i-1] === '/') {
                        modify += 1
                    }
                }

                cur_rel_elevation += modify
                elevation.push(cur_rel_elevation)
                min_elevation = Math.min(min_elevation, cur_rel_elevation)
                max_elevation = Math.max(max_elevation, cur_rel_elevation)
            })

            let height = Math.abs(max_elevation - min_elevation) + 1

            /*----------------------------------------------*
             *
             * paper
             *
             *----------------------------------------------*/
            let max_width = 350
            const os = 10
            const SIZE = (max_width - os*2) / Math.max(4, width)
            max_width = Math.min(350, SIZE*width+os*2)
            const paper = Raphael(dom, max_width, SIZE*height+os*2, 0, 0)

            /*---------------------------------------------*
             *
             * draw grid
             *
             *---------------------------------------------*/
            let hi_mod = diagram[0] !== '\\' ? 0: 1
            let ridge = ['M', os, 
                (height - (elevation[0] - min_elevation + hi_mod))*SIZE+os,]

            const grid_set = paper.set()
            const line_set = paper.set()
            const flood_set = paper.set()

            for (let i=0; i < width; i += 1) {
                for (let j=0; j < height; j += 1) {

                    const elev = elevation[i] - min_elevation + 1

                    // flood
                    if (area[i] && elev === height - j) {
                        flood_set.push(
                            paper.rect(
                                SIZE*i+os,
                                SIZE*j+os,
                                SIZE*(area[i]-i+1), SIZE*(height-j)).attr(
                                    attr.flood.before)
                        )
                        if (width <= 100) {
                            for (let k=i+1; k <= area[i]; k += 1) {
                                line_set.push(
                                    paper.path(
                                        ['M', SIZE*k+os, SIZE*j+os,
                                        'l', 0, SIZE*(height-j)].join(' ')
                                    ).attr( attr.grid.before)
                                )
                            }
                            for (let m=j+1; m < height; m += 1) {
                                line_set.push(
                                    paper.path(
                                        ['M', SIZE*i+os, SIZE*m+os,
                                        'l', SIZE*(area[i]-i), 0].join(' ')
                                    ).attr( attr.grid.before)
                                )
                            }
                        }
                    }

                    // ridge
                    const coord = {'\\': ['l', SIZE, SIZE],
                                    '/': ['l', SIZE, SIZE*-1],
                                    '_': ['l', SIZE, 0]}

                    if (elev === height - j) {
                        ridge = ridge.concat(coord[diagram[i]])
                    }

                    // grid
                    /*
                    if (width < 100) {
                        const m = paper.rect(
                            SIZE*i+os,
                            SIZE*j+os,
                            SIZE, SIZE).attr(attr.grid)
                        grid_set.push(m)
                    }
                    */
                }
            }

            // draw mountain
            ridge = ridge.concat(['L', width*SIZE+os, height*SIZE+os, 
                                    'L', os, height*SIZE+os, 'Z'])
            paper.path(ridge.join(' ')).attr(attr.mountain.content)

            // grid (move front)
            /*
            if (width < 100) {
                grid_set.toFront()
            }
            */

            // draw ridge (again)
            paper.path(ridge.join(' ')).attr(attr.mountain.ridge)

            // flood animation
            if (result) {
                flood_set.attr(attr.flood.after)
                line_set.attr(attr.grid.after)
            }
        }

        var $tryit;
        var io = new extIO({
            multipleArguments: false,
            functions: {
                js: 'floodArea',
                python: 'flood_area'
            },
            animation: function($expl, data){
                floodAreaCanvas(
                    $expl[0],
                    data.in,
                    data,
                );
            }
        });
        io.start();
    }
);
