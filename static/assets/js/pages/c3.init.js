!(function (a) {
    "use strict";
    var t = function () {};
    (t.prototype.init = function () {
        c3.generate({
            bindto: "#chart",
            data: {
                columns: [
                    ["data1", 30, 20, 50, 40, 60, 50],
                    ["data2", 200, 130, 90, 240, 130, 220],
                    ["data3", 300, 200, 160, 400, 250, 250],
                ],
                type: "bar",
                colors: { data1: "#dcdcdc", data2: "#3bc0c3", data3: "#1a2942" },
                color: function (a, t) {
                    return t.id && "data3" === t.id ? d3.rgb(a).darker(t.value / 150) : a;
                },
            },
        }),
            c3.generate({
                bindto: "#combine-chart",
                data: {
                    columns: [
                        ["data1", 30, 20, 50, 40, 60, 50],
                        ["data2", 200, 130, 90, 240, 130, 220],
                        ["data3", 300, 200, 160, 400, 250, 250],
                        ["data4", 200, 130, 90, 240, 130, 220],
                        ["data5", 130, 120, 150, 140, 160, 150],
                    ],
                    types: { data1: "bar", data2: "bar", data3: "spline", data4: "line", data5: "bar" },
                    colors: { data1: "#dcdcdc", data2: "#3bc0c3", data3: "#1a2942", data4: "#E67A77", data5: "#95D7BB" },
                    groups: [["data1", "data2"]],
                },
                axis: { x: { type: "categorized" } },
            }),
            c3.generate({
                bindto: "#roated-chart",
                data: {
                    columns: [
                        ["data1", 30, 200, 100, 400, 150, 250],
                        ["data2", 50, 20, 10, 40, 15, 25],
                    ],
                    types: { data1: "bar" },
                    colors: { data1: "#1a2942", data2: "#3bc0c3" },
                },
                axis: { rotated: !0, x: { type: "categorized" } },
            }),
            c3.generate({
                bindto: "#chart-stacked",
                data: {
                    columns: [
                        ["data1", 30, 20, 50, 40, 60, 50],
                        ["data2", 200, 130, 90, 240, 130, 220],
                    ],
                    types: { data1: "area-spline", data2: "area-spline" },
                    colors: { data1: "#1a2942", data2: "#3bc0c3" },
                },
            });
    }),
        (a.ChartC3 = new t()),
        (a.ChartC3.Constructor = t);
})(window.jQuery),
    (function (a) {
        "use strict";
        window.jQuery.ChartC3.init();
    })();
