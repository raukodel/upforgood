const path = require("path");
const HtmlWebPackPlugin = require("html-webpack-plugin");
const getFilesFromDir = require("./config/files");
const PAGE_DIR = path.join("src", "pages", path.sep);
const webpack = require('webpack')
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

const htmlPlugins = getFilesFromDir(PAGE_DIR, [".html"]).map(filePath => {
    const fileName = filePath.replace(PAGE_DIR, "");
    // { chunks:["contact", "vendor"], template: "src/pages/contact.html",  filename: "contact.html"}
    return new HtmlWebPackPlugin({
        chunks: [fileName.replace(path.extname(fileName), ""), "vendor"],
        template: filePath,
        filename: fileName
    })
});

// { contact: "./src/pages/contact.js" }
const entry = getFilesFromDir(PAGE_DIR, [".js"]).reduce((obj, filePath) => {
    const entryChunkName = filePath.replace(path.extname(filePath), "").replace(PAGE_DIR, "");
    obj[entryChunkName] = `./${filePath}`;
    return obj;
}, {});

module.exports = (env, argv) => ({
    entry: entry,
    output: {
        path: path.join(__dirname, "build"),
        filename: "[name].[hash:4].js"
    },
    devtool: argv.mode === 'production' ? false : 'eval-source-maps',
    plugins: [
        ...htmlPlugins,
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            'window.jQuery': 'jquery'
        }),
        new MiniCssExtractPlugin()
    ],
    resolve: {
        alias: {
            src: path.resolve(__dirname, "src"),
            components: path.resolve(__dirname, "src", "components")
        },
        extensions: ['*', '.js', '.jsx']
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader",
                    options: {
                        presets: [
                            "@babel/preset-env",
                            "@babel/preset-react"
                        ],
                    }
                },
            },
            {
                test: /\.css$/,
                use: [MiniCssExtractPlugin.loader, 'css-loader'],
            },
            {
                test: /\.(svg|jpg|gif|png)$/,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            name: '[name].[ext]',
                            outputPath: (url, resourcePath, context) => {
                                if (argv.mode === 'development') {
                                    const relativePath = path.relative(context, resourcePath);
                                    return `/${relativePath}`;
                                }
                                return `/assets/images/${path.basename(resourcePath)}`;
                            }
                        }
                    }
                ]
            },
            {
                test: /\.(woff|woff2|eot|ttf|otf)$/,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            outputPath: (url, resourcePath, context) => {
                                if (argv.mode === 'development') {
                                    const relativePath = path.relative(context, resourcePath);
                                    return `/${relativePath}`;
                                }
                                return `/assets/fonts/${path.basename(resourcePath)}`;
                            }
                        }
                    }
                ]
            }]
    },
    optimization: {
        minimize: argv.mode === 'production' ? true : false,
        splitChunks: {
            cacheGroups: {
                vendor: {
                    test: /node_modules/,
                    chunks: "initial",
                    name: "vendor",
                    enforce: true
                }
            }
        }
    }
});